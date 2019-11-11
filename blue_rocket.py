"""This module contains BlueRocket class"""

import pygame as pg

from dna import DNA

from rocket import Rocket

class BlueRocket(Rocket):
    """This is the BlueRocket class"""

    def draw(self):
        """Draw the rocket"""
        if self.finished:
            color = pg.color.Color('green1')
        elif self.crushed:
            color = pg.color.Color('indianred1')
        else:
            color = pg.color.Color('red1')
        angle = pg.Vector2(0, 1).angle_to(self.velocity)
        triangles = [pg.Vector2(0, 9), pg.Vector2(-3, -3), pg.Vector2(3, -3)]
        # pg.draw.polygon(pg.display.get_surface(), color, [tr.rotate(angle) for tr in triangles])
        pg.draw.polygon(pg.display.get_surface(), color, [tr.rotate(angle) + self.location for tr in triangles])
