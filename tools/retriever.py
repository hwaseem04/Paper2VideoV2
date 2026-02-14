from pathlib import Path
import json
import logging
import fitz 
import numpy as np
from typing import List, Dict, Optional, Tuple, Any

# Optional imports for embeddings and faiss
try:
    from sentence_transformers import SentenceTransformer
    import faiss
except ImportError:
    SentenceTransformer = None
    faiss = None

from utils.logger import get_logger

class PaperRetriever:
    """
    Retrieves similar papers based on content embeddings.
    """
    def __init__(
        self,
        index_path: Optional[Path] = None,
        model_name: str = "all-MiniLM-L6-v2",
        logger: Optional[logging.Logger] = None
    ):
        self.logger = logger or get_logger("Retriever")
        
        if SentenceTransformer is None or faiss is None:
            self.logger.warning("sentence-transformers or faiss not installed. Retrieval will differ or fail.")
            self.model = None
            self.index = None
        else:
            self.model = SentenceTransformer(model_name)
            self.index = None

        self.papers_metadata: List[Dict] = []
        if index_path and index_path.exists():
            self.load_index(index_path)

    def extract_paper_text(self, pdf_path: Path) -> Dict[str, Any]:
        """
        Extract key sections from a PDF for embedding.
        Returns a dict with 'title', 'abstract', 'content'.
        """
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        
        # Simple heuristic extraction (can be improved with docling/LLM)
        # For now, we treat the first page text as high signal (title/abstract)
        # and the rest as content.
        first_page_text = doc[0].get_text()
        
        return {
            "title": pdf_path.stem, # Fallback to filename if title extraction is hard
            "abstract": first_page_text[:1000], # Approximate
            "content": text,
            "path": str(pdf_path)
        }

    def build_index(self, pdf_paths: List[Path], save_path: Optional[Path] = None):
        """
        Builds a FAISS index from a list of PDF paths.
        """
        if not self.model:
            raise ImportError("sentence-transformers not installed")

        self.logger.info(f"Building index for {len(pdf_paths)} papers...")
        
        embeddings = []
        self.papers_metadata = []

        for i, pdf_path in enumerate(pdf_paths):
            try:
                data = self.extract_paper_text(pdf_path)
                # Embed a combination of title and abstract/start of content
                text_to_embed = f"{data.get('title', '')} {data.get('abstract', '')}"
                
                # Truncate to avoid token limits if necessary (SentenceTransformer handles this mostly)
                embedding = self.model.encode(text_to_embed)
                embeddings.append(embedding)
                
                # Store metadata
                self.papers_metadata.append({
                    "id": i,
                    "path": str(pdf_path),
                    "title": data.get("title", ""),
                    "excerpt": data.get("abstract", "")[:200]
                })
            except Exception as e:
                self.logger.error(f"Failed to process {pdf_path}: {e}")

        if not embeddings:
            self.logger.warning("No embeddings created.")
            return

        embeddings_np = np.array(embeddings).astype('float32')
        dimension = embeddings_np.shape[1]
        
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings_np)
        
        if save_path:
            self.save_index(save_path)
            
        self.logger.info(f"Index built with {self.index.ntotal} documents.")

    def save_index(self, path: Path):
        path = Path(path)
        path.mkdir(parents=True, exist_ok=True)
        
        # Save FAISS index
        faiss.write_index(self.index, str(path / "paper_index.faiss"))
        
        # Save metadata
        with open(path / "paper_metadata.json", "w") as f:
            json.dump(self.papers_metadata, f, indent=2)

    def load_index(self, path: Path):
        path = Path(path)
        if not (path / "paper_index.faiss").exists():
            raise FileNotFoundError(f"Index not found at {path}")
            
        self.index = faiss.read_index(str(path / "paper_index.faiss"))
        
        with open(path / "paper_metadata.json", "r") as f:
            self.papers_metadata = json.load(f)

    def retrieve_similar_papers(self, query: str = None, pdf_path: Path = None, k: int = 5) -> List[Dict]:
        """
        Retrieve top-k similar papers. query can be text string or a PDF path to use as query.
        """
        if not self.model or not self.index:
            raise RuntimeError("Index not loaded or dependencies missing.")

        query_text = ""
        if pdf_path:
            data = self.extract_paper_text(pdf_path)
            query_text = f"{data.get('title', '')} {data.get('abstract', '')}"
        elif query:
            query_text = query
        else:
            raise ValueError("Must provide either query string or pdf_path")

        query_embedding = self.model.encode([query_text]).astype('float32')
        D, I = self.index.search(query_embedding, k)
        
        results = []
        for dist, idx in zip(D[0], I[0]):
            if idx < len(self.papers_metadata) and idx >= 0:
                item = self.papers_metadata[idx].copy()
                item['distance'] = float(dist)
                results.append(item)
                
        return results

if __name__ == "__main__":
    # Test stub
    logging.basicConfig(level=logging.INFO)
    retriever = PaperRetriever()
    print("Retriever initialized.")
