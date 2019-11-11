"""This module contains Rocket class"""

import pygame as pg

from dna import DNA


class Rocket():
    """This is the Rocket class"""

    def __init__(self, start):
        """Constructor"""
        self.dna = None
        self.reset_params(start)

    # Interface segregation principle
    def new(self, grid_scale):
        self.dna = DNA(grid_scale=grid_scale)

    def crossover(self, mutation_scale, a, b):
        self.dna = DNA(mutation_scale=mutation_scale, a=a.dna, b=b.dna)

    def reset_params(self, start):
        """Reset the parameters"""
        self.location = pg.Vector2(start)
        self.velocity = pg.Vector2(0, 0)
        self.max_speed = 6
        self.finished = False
        self.position = None
        self.crushed = False
        self.score = None

    def update(self):
        """Update the Rocket"""
        if not self.finished and not self.crushed:
            acceleration = pg.Vector2(self.dna.get_gene(self.location))
            self.velocity += acceleration
            if self.velocity.length() > self.max_speed:
                self.velocity.scale_to_length(self.max_speed)
            self.location += self.velocity
            w, h = pg.display.get_surface().get_size()
            if not (0 <= self.location.x <= w and 0 <= self.location.y <= h):
                self.crushed = True

    def calc_score(self, target):
        """Calculate the fitness score"""
        dist = self.location.distance_to(target)
        self.score = (1 / self.position if self.finished else 10000) * (1 / dist ** 6) * 10e10
        # if self.finished:
        #     dist = 1
        # self.score = (1 / 10000 * self.finished) * (1 / dist ** 6)
        if self.crushed:
            self.score *= 0.1

    def draw(self):
        """Draw the rocket"""
        if self.finished:
            color = pg.color.Color('green1')
        elif self.crushed:
            color = pg.color.Color('indianred1')
        else:
            color = pg.color.Color('lightblue')
        angle = pg.Vector2(0, 1).angle_to(self.velocity)
        triangles = [pg.Vector2(0, 9), pg.Vector2(-3, -3), pg.Vector2(3, -3)]
        # pg.draw.polygon(pg.display.get_surface(), color, [tr.rotate(angle) for tr in triangles])
        pg.draw.polygon(pg.display.get_surface(), color, [tr.rotate(angle) + self.location for tr in triangles])
