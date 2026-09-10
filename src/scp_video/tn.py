from manim import *

from utils.equations import show_vertical_equations

class TN(Scene):
    display_time = 0.3

    def create_recurrence_def(self):
        recurrence_def = MathTex(
            r"T(n) =",
            r"\begin{cases}",
            r"k_1, & n = 1 \\",
            r"2T(n-1) + k_2, & n > 1",
            r"\end{cases}"
        )

        return recurrence_def

    def create_recurrence(self):
        recurrence = MathTex(r"2T(n-1) + k_2")
        return recurrence

    def construct(self):
        # Def
        recurrence_def = self.create_recurrence_def()

        self.play(FadeIn(recurrence_def))
        self.wait(self.display_time)
        self.play(FadeOut(recurrence_def))

        recurrence = self.create_recurrence()
        rectangle = SurroundingRectangle(recurrence)

        # Recurrence 
        self.play(FadeIn(recurrence))
        self.play(Create(rectangle))

        self.play(
            recurrence.animate.to_edge(UP, buff=0.5),
            rectangle.animate.to_edge(UP, buff=0.4),
        )

        show_vertical_equations(
            self,
            [
                r"T(n-1) = 2T(n-1-1) + k_2",
                r"T(n-1) = 2T(n-2) + k_2",
            ],
            [
                r"T(n) = 2(2T(n-2) +k_2) + k_2",
                r"T(n) = 4T(n-2) + 2k_2 + k_2",
                r"T(n) = 4T(n-2) + 3k_2",
            ],
        )

        show_vertical_equations(
            self,
            [
                r"T(n-2) = 2T(n-1-2) + k_2",
                r"T(n-2) = 2T(n-3) + k_2",
            ],
            [
                r"T(n) = 4(2T(n-3) + k_2) + 3k_2",
                r"T(n) = 8T(n-3) + 4k_2) + 3k_2",
                r"T(n) = 8T(n-3) + 7k_2",
            ],
        )

        show_vertical_equations(
            self,
            [
                r"T(n-2) = 2T(n-1-2) + k_2",
                r"T(n-2) = 2T(n-3) + k_2",
            ],
            [
                r"T(n) = 4(2T(n-3) + k_2) + 3k_2",
                r"T(n) = 8T(n-3) + 4k_2) + 3k_2",
                r"T(n) = 8T(n-3) + 7k_2",
            ],
        )
