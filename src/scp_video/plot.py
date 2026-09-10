from manim import *

import random

# Mock data
N = list(range(1, 101))
times = [
    0.01 * (2 ** (n / 10)) * random.uniform(0.95, 1.05)
    for n in N
]

class Plot(Scene):
    display_time = 1

    def construct(self):
        axes = Axes(
            x_range=[0, 100, 20],
            y_range=[0, max(times) + 1, 1],
            x_length=8,
            y_length=5,
            axis_config={
                #"include_numbers": True,
                "font_size": 10,
            }
        )

        x_label = axes.get_x_axis_label(MathTex("N"))
        y_label = axes.get_y_axis_label(MathTex("Time"))

        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
        )

        graph = VMobject()

        points = [
            axes.c2p(n, time)
            for n, time in zip(N, times)
        ]

        graph.set_points_as_corners(points)
        graph.set_color(BLUE)

        self.play(Create(graph))

        self.wait(2)
        
