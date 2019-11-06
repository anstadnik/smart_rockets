"""This module contains Obstackle class"""

import pygame as pg

class Obstackle(pg.Rect):
    """This the Obstackle class. Rockets hit them"""

    def __init__(self, x, y, w, h):
        """Constructor"""
        super().__init__(x, y, w, h)
        self.color = pg.Color('brown1')

    def contains(self, rocket):
        """Test if rocket is inside the obstacle"""
        return self.collidepoint(rocket.location)

    def draw(self):
        """Draw an obstacle"""
        pg.draw.rect(pg.display.get_surface(), self.color, super())
