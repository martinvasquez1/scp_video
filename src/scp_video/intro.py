from manim import *

class Intro(Scene):
    display_time = 1

    def create_title(self):
        title = Text("Tarea 1 - SCP", font_size=48)
        title.to_edge(UP, buff=2)

        return title

    def create_names(self):
        names = VGroup(
            Text("Name 1", font_size=24),
            Text("Name 2", font_size=24),
            Text("Name 3", font_size=24),
        )
        names.arrange(DOWN, buff=0.2)
        names.to_edge(DOWN, buff=1.2)

        return names

    def construct(self):
        title = self.create_title()
        names = self.create_names()

        self.add(title, names)
        self.wait(self.display_time)
        
        self.play(FadeOut(title), FadeOut(names))
