from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.clock import Clock
import math


class RadarScreen(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.angle = 0

        with self.canvas:

            Color(0,0.8,1,0.4)

            self.circle = Ellipse(
                pos=(100,100),
                size=(250,250)
            )

            self.line = Line(
                width=3
            )

        Clock.schedule_interval(
            self.rotate,
            0.02
        )


    def rotate(self, dt):

        self.angle += 2

        x = 225 + 100 * math.cos(
            math.radians(self.angle)
        )

        y = 225 + 100 * math.sin(
            math.radians(self.angle)
        )

        self.line.points=[
            225,225,x,y
        ]
