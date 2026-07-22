# HashGuard Radar Animation Engine

from kivy.uix.widget import Widget
from kivy.graphics import (
    Color,
    Ellipse,
    Line
)
from kivy.clock import Clock


class Radar(Widget):


    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.angle = 0


        with self.canvas:

            Color(
                0,
                0.8,
                1,
                0.4
            )


            self.circle = Ellipse(
                pos=self.center,
                size=(250,250)
            )


            self.radar_line = Line(
                points=[
                    self.center_x,
                    self.center_y,
                    self.center_x+100,
                    self.center_y
                ],
                width=2
            )


        Clock.schedule_interval(
            self.update_radar,
            0.02
        )



    def update_radar(self, dt):

        self.angle += 2


        import math


        x = (
            self.center_x +
            100 *
            math.cos(
                math.radians(self.angle)
            )
        )


        y = (
            self.center_y +
            100 *
            math.sin(
                math.radians(self.angle)
            )
        )


        self.radar_line.points = [
            self.center_x,
            self.center_y,
            x,
            y
        ]
