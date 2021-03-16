from typing import List

import numpy as np
from pulp import LpVariable, LpBinary, LpConstraint, LpProblem

from model.constraints.constraint_set import ConstraintSet
from model.model import Model, Sense
from problem.problem import Problem


class ModelBuilder:
    """Class that builds the optimization model from a 'business' problem"""

    def __init__(self, constraint_sets: List[ConstraintSet], sense: Sense):
        self._constraint_sets = constraint_sets
        self._sense = sense

    def build(self, problem: Problem) -> Model:
        """Method that builds the model"""

        solver = LpProblem('knapsack', self._sense.value)
        variable_set = self._build_variable_set(problem)
        constraints = self._build_constraints(problem, variable_set)
        objective = self._build_objective(problem, variable_set)

        return Model(
            solver=solver,
            variable_set=variable_set,
            objective=objective,
            constraints=constraints,
            sense=self._sense
        )

    def _build_variable_set(self, problem: Problem) -> np.ndarray:
        """Method that builds the mathematical decision variables"""

        return np.vectorize(
            self._build_bool_var,
            otypes=[np.object]
        )(problem.names)

    def _build_constraints(
            self,
            problem: Problem,
            variable_set: np.ndarray
    ) -> List[LpConstraint]:
        """
        Method that calls the constraint sets and builds the complete
        linear expressions.
        """

        constraints = []

        for constraint_set in self._constraint_sets:
            constraints += constraint_set.build(problem, variable_set)

        return constraints

    @staticmethod
    def _build_objective(
            problem: Problem,
            variable_set: np.ndarray
    ) -> np.ndarray:
        """Method that builds the mathematical objective function"""

        return np.dot(problem.values, variable_set)

    @staticmethod
    def _build_bool_var(name: np.ndarray) -> LpVariable:
        """
        Method that builds a mathematical boolean variable.
        For other optimization frameworks, a similar logic can be applied.

        ** Gurobi

        Model.addVar(lb=0, ub=1, vtype=GRB.BINARY, name=f'x({i}, {j})')

        ** Google or-tools

        Solver.BoolVar(f'x({name})')
        """

        return LpVariable(f'x({name})', 0, 1, LpBinary)
