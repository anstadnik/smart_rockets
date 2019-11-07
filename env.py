"""This module contains Env class"""

import pygame as pg
from params import Parameters
from obstackles import Obstackles
from rockets import Rockets
from tqdm import tqdm

class Env():
    """This the environment class"""

    def __init__(self, args):
        """Constructor"""
        self.params = Parameters(args)
        self.set_up_objects()
        self.counter = 0
        self.generation_counter = 0
        self.generation_pbar = tqdm(leave=True, desc='Generation: ',
                                    bar_format='{desc}{n}', disable=False)
        self.iteration_pbar = tqdm(total=self.params.iteration_duration, leave=False, desc='Living a life', disable=False)

    def set_up_objects(self):
        """Set up the objects"""
        w, h = pg.display.get_surface().get_size()
        self.start = pg.Vector2(w / 2, h - 20)
        self.rockets = Rockets(self.params.grid_scale, self.params.amount, self.start)
        self.obstackles = Obstackles()
        self.target = pg.Vector2(w / 2, 20)

    def add_standart_obstackles(self):
        self.obstackles.add_standart_obstackles()

    def update(self):
        """Update the environment"""
        if self.counter < self.params.iteration_duration:
            self.rockets.update(self.obstackles, self.target)
            self.iteration_pbar.update()
            self.counter += 1
        else:
            self.iteration_pbar.close()
            self.iteration_pbar = tqdm(total=self.params.iteration_duration, leave=False, desc='Living a life', disable=False)
            self.generation_pbar.update()
            self.counter = 0
            self.rockets.evolve(self.params.mutation_scale, self.target)

    def draw(self):
        """Draw everything"""
        # __import__('ipdb').set_trace()
        self.rockets.draw()
        self.obstackles.draw()
        pg.draw.circle(pg.display.get_surface(), pg.color.Color('lightcyan4'),
                       (int(self.target.x), int(self.target.y)), 20)
