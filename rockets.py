"""This module contains Rockets class"""

from random import sample, random

from rocket import Rocket
from blue_rocket import BlueRocket
from red_rocket import RedRocket

# Interface segregation principle
def get_random_rocket(start):
    r = random()
    if r <= 0.33:
        return BlueRocket(start)
    elif r <= 0.66:
        return RedRocket(start)
    return Rocket(start)

def get_new_random_rocket(start, grid_scale):
    rocket = get_random_rocket(start)
    rocket.new(grid_scale)
    return rocket

def get_crossover_random_rocket(start, mutation_scale, a, b):
    rocket = get_random_rocket(start)
    rocket.crossover(mutation_scale, a, b)
    return rocket

class Rockets():
    """This is the Rockets class"""

    def __init__(self, grid_scale, amount, start):
        """Constructor"""
        self.amount = amount
        # Liskov substitution principle
        self.population = [get_new_random_rocket(start, grid_scale) for _ in range(amount)]
        self.start = start
        # self.first
        self.best_result = None
        self.reset_params()

    def reset_params(self):
        """Reset the parameters"""
        self.counter = 0
        self.finished_count = 0
        self.crushed_counter = 0
        self.arrived_counter = 0
        self.first_distance = 0

    def update(self, obstackles, target):
        """Update rockets"""
        for rocket in self.population:
            if rocket.finished or rocket.crushed:
                continue

            rocket.update()

            if obstackles.contains(rocket):
                rocket.crushed = True
                self.crushed_counter += 1

            if rocket.location.distance_to(target) < 20:
                self.finished_count += 1
                rocket.finished = True
                rocket.position = self.finished_count

    def evolve(self, mutation_scale, target):
        """Evolve the population"""
        self.reset_params()
        self.calc_score(target)
        self.crossover(mutation_scale)

    def calc_score(self, target):
        """Precompute the score for all rockets"""
        for rocket in self.population:
            rocket.calc_score(target)

    def crossover(self, mutation_scale):
        """Perform a crossover"""
        mating_pool = []
        total_score = sum([r.score for r in self.population])
        for rocket in self.population:
            score_normal = rocket.score / total_score
            n = int(score_normal * 50000)
            mating_pool.extend([rocket] * n)
        print(len(mating_pool))

        self.population = [get_crossover_random_rocket(self.start, mutation_scale=mutation_scale,
                                                       a=sample(mating_pool, 1)[0], b=sample(mating_pool, 1)[0])
                           for _ in range(self.amount)]

    def draw(self):
        """Draw rectangles"""
        for rocket in self.population:
            rocket.draw()
