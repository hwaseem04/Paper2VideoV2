"""
Build section-wise FAISS indices for targeted retrieval.

This tool:
1. Parses PDFs to detect section headings (Introduction, Methods, Results, etc.)
2. Extracts content for each section
3. Builds separate FAISS indices per section type
4. Stores section metadata for retrieval

Directory structure:
    data_reference/section_indices/
        ├── introduction/
        │   ├── index.faiss
        │   ├── metadata.json
        │   └── doc_map.json
        ├── methodology/
        ├── results/
        └── conclusion/
"""

import sys
from pathlib import Path
import logging
import json
import re
from typing import Dict, List, Optional, Tuple
from tqdm import tqdm
import fitz  # PyMuPDF
import numpy as np

sys.path.append(str(Path(__file__).parent.parent))

from utils.logger import get_logger


class PDFSectionExtractor:
    """Extract sections from academic PDFs based on heading detection."""

    # Standard section names in academic papers
    SECTION_PATTERNS = {
        "introduction": [
            r"^1\.?\s*introduction",
            r"^i\.?\s*introduction",
            r"^\d+\.?\s*introduction",
            r"^introduction\s*$",
        ],
        "methodology": [
            r"^2\.?\s*method",
            r"^3\.?\s*method",
            r"^ii\.?\s*method",
            r"^iii\.?\s*method",
            r"^\d+\.?\s*approach",
            r"^\d+\.?\s*framework",
            r"^\d+\.?\s*model",
            r"^\d+\.?\s*proposed.*method",
            r"^\d+\.?\s*our.*approach",
            r"^method",
        ],
        "results": [
            r"^3\.?\s*result",
            r"^4\.?\s*result",
            r"^5\.?\s*result",
            r"^iii\.?\s*result",
            r"^iv\.?\s*result",
            r"^\d+\.?\s*experiment",
            r"^\d+\.?\s*evaluation",
            r"^\d+\.?\s*performance",
            r"^result",
            r"^experiment",
        ],
        "conclusion": [
            r"^4\.?\s*conclusion",
            r"^5\.?\s*conclusion",
            r"^6\.?\s*conclusion",
            r"^7\.?\s*conclusion",
            r"^\d+\.?\s*conclusion",
            r"^\d+\.?\s*discussion",
            r"^\d+\.?\s*future work",
            r"^conclusion\s*$",
        ],
        "related_work": [
            r"^2\.?\s*related work",
            r"^\d+\.?\s*background",
            r"^\d+\.?\s*literature review",
            r"^\d+\.?\s*prior work",
            r"^\d+\.?\s*related.*work",
            r"^related work",
        ]
    }

    def __init__(self, logger: Optional[logging.Logger] = None):
        self.logger = logger or get_logger("PDFSectionExtractor")

    def extract_sections(self, pdf_path: Path) -> Dict[str, Dict]:
        """
        Extract sections from a PDF.

        Returns:
            Dict mapping section names to:
                {
                    "text": str,
                    "pages": List[int],
                    "start_page": int,
                    "end_page": int
                }
        """
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF not found: {pdf_path}")

        doc = fitz.open(pdf_path)

        # Step 1: Detect section boundaries
        section_boundaries = self._detect_section_boundaries(doc)

        # Step 2: Extract content for each section
        sections = {}
        for section_name, (start_page, end_page) in section_boundaries.items():
            text = self._extract_text_range(doc, start_page, end_page)
            sections[section_name] = {
                "text": text,
                "pages": list(range(start_page, end_page + 1)),
                "start_page": start_page,
                "end_page": end_page,
                "char_count": len(text),
                "word_count": len(text.split())
            }

        doc.close()

        return sections

    def _detect_section_boundaries(self, doc: fitz.Document) -> Dict[str, Tuple[int, int]]:
        """
        Detect section start and end pages.

        Returns:
            Dict mapping section_name -> (start_page, end_page)
        """
        boundaries = {}
        section_starts = {}

        # Scan through pages to find section headings
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()

            # Check each line for section headings
            lines = text.split('\n')
            for line in lines[:20]:  # Check first 20 lines of each page
                line_clean = line.strip().lower()

                # Skip empty lines
                if not line_clean:
                    continue

                # Check against patterns
                for section_name, patterns in self.SECTION_PATTERNS.items():
                    for pattern in patterns:
                        if re.match(pattern, line_clean):
                            section_starts[section_name] = page_num
                            self.logger.info(f"Found '{section_name}' at page {page_num}: {line.strip()[:50]}")
                            break

        # Define boundaries: each section ends where the next begins
        sorted_sections = sorted(section_starts.items(), key=lambda x: x[1])

        for i, (section_name, start_page) in enumerate(sorted_sections):
            if i < len(sorted_sections) - 1:
                # End page is one before next section
                next_start = sorted_sections[i + 1][1]
                end_page = max(start_page, next_start - 1)  # Ensure end >= start
            else:
                # Last section: extend to end of doc (or reasonable limit)
                # Exclude references (usually last 10-20% of paper)
                estimated_end = min(start_page + 10, int(len(doc) * 0.85), len(doc) - 1)
                end_page = max(start_page, estimated_end)  # Ensure end >= start

            boundaries[section_name] = (start_page, end_page)

        return boundaries

    def _extract_text_range(self, doc: fitz.Document, start_page: int, end_page: int) -> str:
        """Extract text from a range of pages."""
        text_parts = []

        for page_num in range(start_page, min(end_page + 1, len(doc))):
            page = doc[page_num]
            text_parts.append(page.get_text())

        return "\n\n".join(text_parts)


class SectionIndexBuilder:
    """Build separate FAISS indices for each section type."""

    def __init__(
        self,
        dataset_dir: Path,
        output_dir: Path,
        logger: Optional[logging.Logger] = None
    ):
        self.dataset_dir = Path(dataset_dir)
        self.output_dir = Path(output_dir)
        self.logger = logger or get_logger("SectionIndexBuilder")

        self.extractor = PDFSectionExtractor(logger=logger)

        # Section-wise storage
        self.section_docs = {
            "introduction": [],
            "methodology": [],
            "results": [],
            "conclusion": [],
            "related_work": []
        }

        self.section_metadata = {section: [] for section in self.section_docs.keys()}

    def build(self, limit: Optional[int] = None):
        """Build section-wise FAISS indices."""

        # Find all PDFs in dataset
        pdf_files = list(self.dataset_dir.rglob("*.pdf"))

        if limit:
            pdf_files = pdf_files[:limit]

        self.logger.info(f"Processing {len(pdf_files)} PDFs for section extraction...")

        # Step 1: Extract sections from all papers
        for pdf_path in tqdm(pdf_files, desc="Extracting sections"):
            try:
                sections = self.extractor.extract_sections(pdf_path)

                # Store each section
                for section_name, section_data in sections.items():
                    if section_name in self.section_docs:
                        self.section_docs[section_name].append(section_data["text"])
                        self.section_metadata[section_name].append({
                            "pdf_path": str(pdf_path),
                            "pdf_name": pdf_path.stem,
                            "pages": section_data["pages"],
                            "start_page": section_data["start_page"],
                            "end_page": section_data["end_page"],
                            "word_count": section_data["word_count"]
                        })

            except Exception as e:
                self.logger.error(f"Failed to process {pdf_path.name}: {e}")

        # Step 2: Build FAISS index for each section
        self.logger.info("\nBuilding FAISS indices...")

        for section_name in self.section_docs.keys():
            docs = self.section_docs[section_name]
            metadata = self.section_metadata[section_name]

            if not docs:
                self.logger.warning(f"No documents found for section '{section_name}'. Skipping.")
                continue

            self.logger.info(f"Building index for '{section_name}' ({len(docs)} documents)...")

            # Create section output directory
            section_dir = self.output_dir / section_name
            section_dir.mkdir(parents=True, exist_ok=True)

            # Build FAISS index
            index, embeddings = self._build_faiss_index(docs)

            # Save index
            import faiss
            faiss.write_index(index, str(section_dir / "index.faiss"))

            # Save metadata
            with open(section_dir / "metadata.json", "w") as f:
                json.dump(metadata, f, indent=2)

            # Save document map (for debugging)
            doc_map = {
                "section_name": section_name,
                "num_documents": len(docs),
                "embedding_dim": embeddings.shape[1] if embeddings is not None else 0,
                "papers": [m["pdf_name"] for m in metadata]
            }

            with open(section_dir / "doc_map.json", "w") as f:
                json.dump(doc_map, f, indent=2)

            self.logger.info(f"✓ Saved {section_name} index with {len(docs)} documents")

        # Step 3: Save global summary
        summary = {
            "total_papers": len(pdf_files),
            "sections": {
                section: {
                    "num_documents": len(self.section_docs[section]),
                    "index_path": str(self.output_dir / section / "index.faiss")
                }
                for section in self.section_docs.keys()
            }
        }

        with open(self.output_dir / "section_index_summary.json", "w") as f:
            json.dump(summary, f, indent=2)

        self.logger.info(f"\n✓ Section-wise indices built at {self.output_dir}")

    def _build_faiss_index(self, documents: List[str]) -> Tuple:
        """Build FAISS index from documents."""
        try:
            from sentence_transformers import SentenceTransformer
            import faiss
        except ImportError:
            self.logger.error("Please install: pip install sentence-transformers faiss-cpu")
            return None, None

        # Load embedding model
        model = SentenceTransformer('all-MiniLM-L6-v2')

        # Generate embeddings
        self.logger.info(f"Generating embeddings for {len(documents)} documents...")
        embeddings = model.encode(documents, show_progress_bar=True)
        embeddings = np.array(embeddings).astype('float32')

        # Normalize for cosine similarity
        faiss.normalize_L2(embeddings)

        # Build FAISS index
        dim = embeddings.shape[1]
        index = faiss.IndexFlatIP(dim)  # Inner product (cosine similarity after normalization)
        index.add(embeddings)

        return index, embeddings


def build_section_indices(
    dataset_dir: str = "dataset",
    output_dir: str = "data_reference/section_indices",
    limit: Optional[int] = None
):
    """
    Main entry point to build section-wise FAISS indices.

    Args:
        dataset_dir: Directory containing PDF files
        output_dir: Where to save section indices
        limit: Max number of PDFs to process (None for all)
    """
    logging.basicConfig(level=logging.INFO)
    logger = get_logger("SectionIndexBuilder")

    dataset_path = Path(dataset_dir)
    output_path = Path(output_dir)

    if not dataset_path.exists():
        logger.error(f"Dataset directory not found: {dataset_path}")
        return

    builder = SectionIndexBuilder(
        dataset_dir=dataset_path,
        output_dir=output_path,
        logger=logger
    )

    builder.build(limit=limit)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Build section-wise FAISS indices")
    parser.add_argument("--dataset", type=str, default="dataset", help="Dataset directory")
    parser.add_argument("--output", type=str, default="data_reference/section_indices", help="Output directory")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of PDFs")

    args = parser.parse_args()

    build_section_indices(
        dataset_dir=args.dataset,
        output_dir=args.output,
        limit=args.limit
    )
