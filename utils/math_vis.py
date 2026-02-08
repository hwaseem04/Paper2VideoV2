from manim import *
from pydub import AudioSegment
import textwrap
from moviepy.editor import VideoFileClip
class Math_visual(Scene):
    def __init__(self, plan=None):
        super().__init__()
        self.plan = plan
    def construct(self):
        # Title for the formula
        if "scenario" in self.plan:
            title = Text(self.plan["scenario"], font_size=36).to_edge(UP)
            self.play(FadeIn(title))

        col_width   = config.frame_width / 3
        col_center  = RIGHT * (config.frame_width / 3)

        wrapped_lines = textwrap.fill(self.plan["audio_content"], width=20).splitlines()

        ruler = Text("A"*20, font_size=80)
        for font in range(80, 9, -2):
            ruler.font_size = font
            if ruler.width <= col_width - 0.4:
                break
        optimal_font = font

        paragraph = Paragraph(
            *wrapped_lines,           
            font_size=optimal_font,
            line_spacing=1.3,
            alignment="center"
        )

        paragraph.move_to(col_center)

        self.play(FadeIn(paragraph))
    
        self.animate()

    def animate(self):
        # Define a simple circle
        circle = Circle(radius=1, color="BLUE")
    
        # Define a simple square
        square = Square(side_length=2, color="RED")
        square.shift(RIGHT * 2)
    
        # Create animations
        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Rotate(square, angle=PI/2))
        self.play(FadeOut(square))
    
        self.wait(3)



# Main rendering function that returns the video
def render_video(dir, plan):
    config.media_dir = dir  # Set media directory
    config.output_file = "scene.mp4"  # Set output file name
    scene = Math_visual(plan)  # Create scene
    scene.render()  # Render the video
    return config.output_file  # Return the generated video file path

    
