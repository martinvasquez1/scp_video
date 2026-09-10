from manim import *

# Mock data
data = [
    ["5",  "3", "2", "8",  "Sí", "{1,3}", "12",  "0.42"],
    ["10", "5", "2", "21", "Sí", "{2,4}", "37",  "1.18"],
    ["15", "8", "3", "47", "No", "—",     "152", "4.73"],
    ["15", "8", "3", "47", "No", "—",     "152", "4.73"],
    ["15", "8", "3", "47", "No", "—",     "152", "4.73"],
    ["15", "8", "3", "47", "No", "—",     "152", "4.73"],
    ["15", "8", "3", "47", "No", "—",     "152", "4.73"],
    ["15", "8", "3", "47", "No", "—",     "152", "4.73"],
    ["15", "8", "3", "47", "No", "—",     "152", "4.73"],
    ["15", "8", "3", "47", "No", "—",     "152", "4.73"],
]

headers = [
    "m",
    "n",
    "k",
    "Relaciones",
    "Solución",
    "Ubicaciones",
    "Recursiones",
    "Tiempo (ms)"
]

class TableResults(Scene):
    def construct(self):
        table = Table(
            data,
            col_labels=[Text(h, font_size=22) for h in headers],
            include_outer_lines=True,
            line_config={"stroke_width": 1.1},
            element_to_mobject=lambda x: Text(
                str(x),
                font_size=24,
            )
        )

        table.scale(0.6)

        self.play(Create(table.get_horizontal_lines()))
        self.play(Create(table.get_vertical_lines()))

        self.play(
            LaggedStart(
                *[Write(cell) for cell in table.get_col_labels()],
                lag_ratio=0.1
            )
        )

        for row in table.get_rows()[1:]:
            self.play(
                LaggedStart(
                    *[Write(cell) for cell in row],
                    lag_ratio=0.001
                )
            )

        n_column = table.get_columns()[7]
        self.play(n_column.animate.set_color(YELLOW))

        self.wait(2)
