from typing import List

import numpy as np
from pulp import LpConstraint

from problem.problem import Problem


class ConstraintSet:
    """Class to set the signature that builds a constraint set"""

    def build(
            self,
            problem: Problem,
            variable_set: np.ndarray
    ) -> List[LpConstraint]:
        """Method to implement a particular constraint set"""

        pass
