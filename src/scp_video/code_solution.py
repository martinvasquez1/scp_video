from manim import *

class CodeSolution(Scene):
    def construct(self):
        pseudocode = Code(
            "scp.py",
            language="python",
            background="rectangle",
        )
        
        pseudocode.scale(0.6)

        self.play(Create(pseudocode))
        self.wait(2)

        self.play(FadeOut(pseudocode))
