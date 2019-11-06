"""This module contains Env class"""

import pygame as pg
from params import Parameters
from obstackles import Obstackles
from rockets import Rockets

class Env():
    """This the environment class"""

    def __init__(self, args):
        """Constructor"""
        self.params = Parameters(args)
        self.set_up_objects()
        self.counter = 0

    def set_up_objects(self):
        """Set up the objects"""
        w, h = pg.display.get_surface().get_size()
        print(w, h)
        self.start = pg.Vector2(w / 2, h - 20)
        self.rockets = Rockets(self.params.grid_scale, self.params.amount, self.start)
        self.obstackles = Obstackles()
        self.target = pg.Vector2(w / 2, h - 20)

    def add_standart_obstackles(self):
        self.obstackles.add_standart_obstackles()

    def update(self):
        """Update the environment"""
        if self.counter < self.params.iteration_duration:
            self.rockets.update(self.obstackles, self.target)
            self.counter += 1
        else:
            self.counter = 0
            self.rockets.evolve(self.params.mutation_scale, self.target)

    def draw(self):
        """Draw everything"""
        # __import__('ipdb').set_trace()
        self.rockets.draw()
        self.obstackles.draw()
        # pg.draw.circle(pg.display.get_surface(), pg.color.Color('lightcyan4'),
        #                (int(self.target.x), int(self.target.y)), 20)
