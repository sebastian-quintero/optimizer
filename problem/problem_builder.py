import numpy as np

from problem.problem import Problem
from schema.knapsack import Knapsack


class ProblemBuilder:
    """Class that builds the 'business' knapsack problem from the request"""

    def build(self, knapsack: Knapsack) -> Problem:
        """Method that builds the problem"""

        size = len(knapsack.items)
        capacity = knapsack.capacity
        names = np.empty(size, dtype='<U100')
        weights = np.zeros(size)
        values = np.zeros(size)

        for ix, item in enumerate(knapsack.items):
            names[ix] = item.name
            weights[ix] = item.weight
            values[ix] = item.value

        return Problem(
            capacity=capacity,
            names=names,
            weights=weights,
            values=values
        )
