"""This module contains DNA class"""

from random import random

import pygame as pg

from helpers import rand_vec2, constrain

class DNA():
    """This is the DNA class"""

    def __init__(self, *, grid_scale=None, mutation_scale=None, a=None, b=None):
        """Constructor"""
        if grid_scale is not None:
            w, h = pg.display.get_surface().get_size()
            w, h = w // grid_scale, h // grid_scale
            self.genes = [[rand_vec2() for w in range(w)] for _ in range(h)]
            self.grid_scale = grid_scale
        elif mutation_scale is not None and a is not None and b is not None:
            assert len(a) == len(b)
            assert len(a[0]) == len(b[0])
            self.grid_scale = a.grid_scale
            self.genes = [[a.genes[h_][w_] if random() < 0.5 else b.genes[h_][w_]
                           for w_ in range(len(a[0]))]
                          for h_ in range(len(a))]
            self.mutate(mutation_scale)
        else:
            raise RuntimeError('You should either provide grid_scale or parameters for crossover')

    def mutate(self, mutation_scale):
        """Set some genes to random values with given probability"""
        self.genes = [[g if random() < mutation_scale else rand_vec2() for g in l]
                      for l in self.genes]

    def get_gene(self, position):
        """Get gene by position"""
        x, y = position
        x = constrain(x, 0, len(self.genes) - 1)
        y = constrain(y, 0, len(self.genes[0]) - 1)
        return self.genes[x][y]
