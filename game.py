"""This file contains the main game class"""
import pygame as pg
from env import Env

class Game():
    """This is the main game class"""

    def __init__(self, args):
        """Constructor"""
        self.args = args
        self.set_up_pylint()
        self.env = Env(args)
        #  TODO: Add paused, adding <06-11-19, astadnik> #
        self.reset_params()

    def set_up_pylint(self):
        """Set up everything that is needed for pylint"""
        self.fps = 60
        self.clock = pg.time.Clock()
        pg.init()
        pg.display.set_caption("Smart Rockets")
        self.screen = pg.display.set_mode((640, 480))

    def reset_params(self):
        self.paused = False
        self.adding = False
        self.standart_obs_added = False

    def run(self):
        """Combine everything together"""
        while True:
            self.screen.fill(pg.Color('darkturquoise'))
            if not self.paused:
                self.env.update()
            self.env.draw()
            if self.handle_input():
                return
            pg.display.flip()
            self.clock.tick(self.fps)

    def handle_input(self):
        """Handles input"""
        #  TODO: Add more controls <06-11-19, astadnik> #
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    return True
                if event.key == pg.K_p:
                    paused = not paused
                if event.key == pg.K_s and not standart_obs_added:
                    standart_obs_added = True
                    self.env.add_standart_obstackles()

                if event.key == pg.K_r:
                    self.reset_params()
                    self.env = Env(self.args)

        return False
