from manim import *

class Context(Scene):
    def construct(self):
        description = Paragraph(
            "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod\n ipsum dolor sit amet consectetur adipiscing",
            alignment="center",
            font_size=20
        )

        description.to_edge(UP)

        self.play(FadeIn(description))
        self.wait(2)

        # Set
        numbers = VGroup(
            MathTex("1"),
            MathTex("2"),
            MathTex("3"),
            MathTex("4"),
            MathTex("5"),
        )

        numbers[0].move_to(LEFT * 2.0 + UP)
        numbers[1].move_to(RIGHT * 2.0 + UP)
        numbers[2].move_to(LEFT * 1.0)
        numbers[3].move_to(RIGHT * 1.0)
        numbers[4].move_to(DOWN * 2.0)

        self.play(
            LaggedStart(
                *[Write(n) for n in numbers],
                lag_ratio=0.15
            )
        )

        subset_1 = Ellipse(
            width=5,
            height=3.5,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.10,
        )
        subset_1_target = VGroup(numbers[2], numbers[4]) 

        subset_1.move_to(subset_1_target.get_center())
        subset_1.shift(RIGHT * 0.5)

        self.play(Create(subset_1))

        # Sub 2
        subset_2 = Circle(
            radius=0.5,
            color=RED,
            fill_color=RED,
            fill_opacity=0.10,
        )

        subset_2.move_to(numbers[0])
        self.play(Create(subset_2))

        # Sub 3
        subset_3 = Circle(
            radius=0.5,
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0.10,
        )

        subset_3.move_to(numbers[1])
        self.play(Create(subset_3))

        # Sub 4
        subset_4 = Circle(
            radius=0.5,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=0.10,
        )

        subset_4.move_to(numbers[4])
        self.play(Create(subset_4))
