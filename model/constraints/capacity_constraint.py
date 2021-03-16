from typing import List

import numpy as np
from pulp import LpConstraint

from model.constraints.constraint_set import ConstraintSet
from problem.problem import Problem


class CapacityConstraint(ConstraintSet):
    """Class that represents the maximum capacity constraint"""

    def build(
            self,
            problem: Problem,
            variable_set: np.ndarray
    ) -> List[LpConstraint]:
        """
        Method that builds all the constraints in the set,
        independent of the optimization framework
        """

        weighted_items = np.dot(variable_set, problem.weights)
        constraints = [weighted_items <= problem.capacity]

        return constraints
