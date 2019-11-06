"""This module contains Rockets class"""

from random import sample

from rocket import Rocket


class Rockets():
    """This is the Rockets class"""

    def __init__(self, grid_scale, amount, start):
        """Constructor"""
        self.amount = amount
        self.population = [Rocket(start, grid_scale=grid_scale) for _ in range(amount)]
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

        self.population = [Rocket(self.start, mutation_scale=mutation_scale,
                                  a=sample(mating_pool, 1), b=sample(mating_pool, 1))]

    def draw(self):
        """Draw rectangles"""
        for rocket in self.population:
            rocket.draw()
