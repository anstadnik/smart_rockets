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
            self.genes = [[rand_vec2() for _ in range(w)] for _ in range(h)]
            self.grid_scale = grid_scale
        elif mutation_scale is not None and a is not None and b is not None:
            assert len(a.genes) == len(b.genes)
            assert len(a.genes[0]) == len(b.genes[0])
            self.grid_scale = a.grid_scale
            self.genes = [[a.genes[h_][w_] if random() < 0.5 else b.genes[h_][w_]
                           for w_ in range(len(a.genes[0]))]
                          for h_ in range(len(a.genes))]
            self.mutate(mutation_scale)
        else:
            raise RuntimeError('You should either provide grid_scale or parameters for crossover')

    def mutate(self, mutation_scale):
        """Set some genes to random values with given probability"""
        self.genes = [[g if random() > mutation_scale else rand_vec2() for g in l]
                      for l in self.genes]

    def get_gene(self, position):
        """Get gene by position"""
        x, y = position
        # print(position)
        x /= self.grid_scale
        y /= self.grid_scale
        # print(x, y)
        x = constrain(int(x), 0, len(self.genes[0]) - 1)
        y = constrain(int(y), 0, len(self.genes) - 1)
        # print(x, y)
        # print(len(self.genes[0]) - 1, len(self.genes) - 1)
        # input()
        return self.genes[y][x]

    # def draw(self):
    #     for y in range(len(self.genes)):
    #         for x in range(len(self.genes[i])):
    #             angle = pg.Vector2(0, 1).angle_to(self.vec)
    #             pos = grid_scale * x, grid_scale * y
    #             # line 
    #             # triangles = [pg.Vector2(0, 9), pg.Vector2(-3, -3), pg.Vector2(3, -3)]
    #             # triangles = [pg.Vector2(0, 9), pg.Vector2(-3, -3), pg.Vector2(3, -3)]
    #             # pg.draw.polygon(pg.display.get_surface(), color, [tr.rotate(angle) for tr in triangles])
    #             pg.draw.polygon(pg.display.get_surface(), color, [tr.rotate(angle) + self.location for tr in triangles])
