from dataclasses import dataclass
from enum import IntEnum
from typing import List, Tuple

import numpy as np
from pulp import LpStatusOptimal, LpConstraint, LpProblem, LpVariable, value, \
    PULP_CBC_CMD

from problem.problem import Problem


class Sense(IntEnum):
    """Class that enumerates the possible optimization senses"""

    MINIMIZATION = 1
    MAXIMIZATION = -1


@dataclass
class ModelSolution:
    """Class that represents the numerical solution of the model"""

    variable_set: np.ndarray
    objective: float
    solution_value: float = 0.99

    def parse(self, problem: Problem) -> Tuple[List[str], float, float]:
        """Method to parse the mathematical solution to an interpretable one"""

        selected_items_ix = np.where(self.variable_set >= self.solution_value)
        selected_items = problem.names[selected_items_ix].tolist()
        total_weight = problem.weights[selected_items_ix].sum()

        return selected_items, self.objective, total_weight


@dataclass
class Model:
    """Class that represents a computational optimization model"""

    solver: LpProblem
    variable_set: np.ndarray
    objective: np.ndarray
    constraints: List[LpConstraint]
    sense: Sense

    def solve(self) -> ModelSolution:
        """
        Method to solve the optimization model.
        For other optimization frameworks, a similar logic can be applied.

        ** Gurobi

        for constraint in self.constraints:
            self.solver.addConstr(constraint)

        self.solver.setObjective(self.objective, self.sense)
        self.solver.optimize()

        if self.engine_model.status == GRB.OPTIMAL:
            solution = np.vectorize(self._var_sol)(self.variable_set)
        else:
            solution = np.array([])

        ** Google or-tools

        for constraint in self.constraints:
            self.solver.Add(constraint)

        if self.sense == Sense.MINIMIZATION:
            self.solver.Minimize(self.objective)
        else:
            self.solver.Maximize(self.objective)

        status = self.solver.Solve()

        if status == Solver.OPTIMAL:
            solution = np.vectorize(self.var_sol)(self.variable_set)
        else:
            solution = np.array([])
        """
        for constraint in self.constraints:
            self.solver += constraint

        self.solver += self.objective

        status = self.solver.solve(PULP_CBC_CMD(msg=False))

        if status == LpStatusOptimal:
            solution = np.vectorize(self._var_sol)(self.variable_set)
        else:
            solution = np.array([])

        return ModelSolution(
            variable_set=solution,
            objective=self.solver.objective.value()
        )

    @staticmethod
    def _var_sol(var: LpVariable) -> float:
        """
        Method to obtain the solution value of a variable.
        For other optimization frameworks, a similar logic can be applied.

        ** Gurobi

        var.x

        ** Google or-tools

        var.solution_value()
        """

        return value(var)
