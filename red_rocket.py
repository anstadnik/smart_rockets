"""This module contains RedRocket class"""

import pygame as pg

from rocket import Rocket

# Open-Closed principle
# No need to change the Rocket for deriving from that

class RedRocket(Rocket):
    """This is the RedRocket class"""

    def draw(self):
        """Draw the rocket"""
        if self.finished:
            color = pg.color.Color('green1')
        elif self.crushed:
            color = pg.color.Color('indianred1')
        else:
            color = pg.color.Color('blue1')
        angle = pg.Vector2(0, 1).angle_to(self.velocity)
        triangles = [pg.Vector2(0, 9), pg.Vector2(-3, -3), pg.Vector2(3, -3)]
        # pg.draw.polygon(pg.display.get_surface(), color, [tr.rotate(angle) for tr in triangles])
        pg.draw.polygon(pg.display.get_surface(), color, [tr.rotate(angle) + self.location for tr in triangles])
