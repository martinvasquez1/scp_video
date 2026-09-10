from manim import *

from utils.equations import show_equation

class TNSolution(Scene):
    display_time = 0.3

    def construct(self):
        pattern = MathTex(r"2^i T(n-i) + (2^i - 1)k_2")

        self.play(FadeIn(pattern))
        self.play(pattern.animate.to_corner(UL, buff=0.5))

        # Solve i
        solve_i = show_equation(
            self,
            [
                r"T(n-i) = T(1)",
                r"n-i = 1",
                r"i = n - 1",
            ],
        )

        self.play(solve_i.animate.to_corner(UR, buff=0.5))

        # Solution
        solution = show_equation(
            self,
            [
                r"2^i T(n-i) + (2^i-1)k_2",
                r"2^{n-1}T(n-(n-1)) + (2^{n-1}-1)k_2",
                r"2^{n-1}T(1) + (2^{n-1}-1)k_2",
                r"2^{n-1}k_1 + (2^{n-1}-1)k_2",
            ],
        )

        self.wait(2)

        self.play(
            FadeOut(
                pattern,
                solve_i,
                solution
            )
        )
