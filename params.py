"""This module contains Parameters class"""

class Parameters():
    """This class holds all parameters"""

    def __init__(self, args):
        """Constructor"""
        self.args = args
        self.reset_params()

    def reset_params(self):
        """Reset params"""
        self.iteration_duration = self.args.iteration_duration
        self.speed = self.args.speed
        self.grid_scale = self.args.grid_scale
        self.amount = self.args.amount
        self.mutation_scale = self.args.mutation_scale
