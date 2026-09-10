from manim import *

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

    def do_replacement(self, replacement_arr, sustitution_arr):
        # Replace
        replacement_1_1 = MathTex(r"T(n-1) = 2T(n-1-1) + k2")
        replacement_1_2 = MathTex(r"T(n-1) = 2T(n-2) + k2")

        self.play(FadeIn(replacement_1_1))
        self.wait(self.display_time * 2)

        replacement_1_2.next_to(replacement_1_1, DOWN)
        self.play(FadeIn(replacement_1_2))

        replacements_1 = VGroup(replacement_1_1, replacement_1_2)
        self.play(replacements_1.animate.shift(UP*2))

        # Sus
        sustitution_1_1 = MathTex(r"T(n) = 2(2T(n-2) +k2) + k2")
        sustitution_1_2 = MathTex(r"T(n) = 4T(n-2) + 2k + k2")
        sustitution_1_3 = MathTex(r"T(n) = 4T(n-2) + 3k")

        self.play(FadeIn(sustitution_1_1))
        self.wait(self.display_time * 2)

        sustitution_1_2.next_to(sustitution_1_1, DOWN)
        self.play(FadeIn(sustitution_1_2))

        sustitution_1_3.next_to(sustitution_1_2, DOWN)
        self.play(FadeIn(sustitution_1_3))

        self.wait(self.display_time * 2)

    def construct(self):
        # Def
        recurrence_def = self.create_recurrence_def()

        self.play(FadeIn(recurrence_def))
        self.wait(self.display_time)
        self.play(FadeOut(recurrence_def))

        recurrence = self.create_recurrence()
        rectangle = SurroundingRectangle(recurrence)

        # Rec
        self.play(FadeIn(recurrence))
        self.play(Create(rectangle))

        self.play(
            recurrence.animate.to_edge(UP, buff=0.5),
            rectangle.animate.to_edge(UP, buff=0.4),
        )

        a = ["12321", "111", "222"]
        b = ["999", "1111111111", "777"]
        self.do_replacement(a, b)
