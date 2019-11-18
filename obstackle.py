"""This module contains Obstackle class"""

import pygame as pg
from entity import Entity

# Single responsibility principle

class DrawableRect(Entity, pg.Rect):
    """This is the DrawableRect class"""
    def __init__(self, x, y, w, h):
        """Constructor"""
        super().__init__(x, y, w, h)
        self.color = pg.Color('brown1')

    def draw(self):
        """Draw an obstacle"""
        pg.draw.rect(pg.display.get_surface(), self.color, self)


class Obstackle(DrawableRect):
    """This the Obstackle class. Rockets hit them"""

    def contains(self, rocket):
        """Test if rocket is inside the obstacle"""
        return self.collidepoint(rocket.location)
