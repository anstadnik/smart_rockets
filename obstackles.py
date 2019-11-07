"""This module contains Obstackles class"""

from obstackle import Obstackle
import pygame as pg

class Obstackles():
    """This the Obstackles class which manages list of obstacles"""

    def __init__(self):
        """Constructor"""
        self.obstackles = []

    def draw(self):
        """Display obstackles"""
        for obs in self.obstackles:
            obs.draw()

    def add_obstackle(self, x, y, w, h):
        """Add an obstackle"""
        self.obstackles.append(Obstackle(x, y, w, h))

    def add_standart_obstackles(self):
        w, _ = pg.display.get_surface().get_size()
        self.add_obstackle(0, 200, 170, 20)
        self.add_obstackle(230, 200, w - 230, 20)
        self.add_obstackle(0, 400, 320, 20)
        self.add_obstackle(380, 400, w - 380, 20)
        self.add_obstackle(0, 600, 470, 20)
        self.add_obstackle(530, 600, w - 530, 20)

    def contains(self, rocket):
        """Test if rocket is inside any of the obstackles"""
        for obs in self.obstackles:
            if obs.contains(rocket):
                return True
        return False
