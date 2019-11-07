"""This module contains utility functions"""

from random import random
import argparse
import pygame as pg

def parse():
    """Parses inputs"""
    parser = argparse.ArgumentParser(description='Smart rockets')
    parser.add_argument("--iteration_duration", default=500, help="TODO")
    parser.add_argument("--speed", default=1, help="TODO")
    parser.add_argument("--grid_scale", default=10, help="TODO")
    parser.add_argument("--amount", default=1000, help="TODO")
    parser.add_argument("--mutation_scale", default=0.02, help="TODO")
    return parser.parse_args()

def rand_vec2():
    """Get random normalized vector"""
    return pg.Vector2(1 - 2 * random(), 1 - 2 * random()).normalize()

def constrain(val, minimum, maximum):
    """Constrain a variable to be bigger than minimum and less then maximum"""
    return min(max(val, minimum), maximum)
