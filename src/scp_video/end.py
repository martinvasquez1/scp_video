from manim import *

class End(Scene):
    display_time = 1

    def construct(self):
        title = Text("Conclusión", font_size=48)
        title.to_edge(UP, buff=2)

        self.play(FadeIn(title))

        description = Paragraph(
            "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod",
            "ipsum dolor sit amet consectetur adipiscing elit",
            alignment="center",
            font_size=20,
        )

        self.play(FadeIn(description))
