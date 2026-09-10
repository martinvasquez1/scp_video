from manim import *

class Pseudocode(Scene):
    def construct(self):
        pseudocode = Code(
            "pseudocode.txt",
            language="text",
            background="rectangle",
        )
        
        pseudocode.to_corner(UL)
        self.play(Create(pseudocode))
        self.wait(2)
        self.play(FadeOut(pseudocode))
