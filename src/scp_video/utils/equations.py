from manim import *

def show_equation(self, equations):
    texts = [MathTex(equation) for equation in equations]

    for i, text in enumerate(texts):
        if i > 0:
            text.next_to(texts[i - 1], DOWN)

        self.play(FadeIn(text))

    return VGroup(*texts)

def show_vertical_equations(self, a, b):
    first_group = show_equation(self, a)
    self.play(first_group.animate.shift(UP * 2))

    second_group = show_equation(self, b)
    self.wait(self.display_time * 2)

    groups = VGroup(first_group, second_group)
    self.play(FadeOut(groups))
    self.wait(self.display_time)
