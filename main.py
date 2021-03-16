import uvicorn
from fastapi import FastAPI

from model.constraints.capacity_constraint import CapacityConstraint
from model.model import Sense
from model.model_builder import ModelBuilder
from problem.problem_builder import ProblemBuilder
from schema.knapsack import Knapsack

optimizer = FastAPI()


@optimizer.post("/knapsack/")
async def optimize(knapsack: Knapsack):
    """Optimize the knapsack problem"""

    problem_builder = ProblemBuilder()
    model_builder = ModelBuilder(
        constraint_sets=[CapacityConstraint()],
        sense=Sense.MAXIMIZATION
    )
    problem = problem_builder.build(knapsack)
    model = model_builder.build(problem)
    solution = model.solve()
    selected_items, total_value, total_weight = solution.parse(problem)

    return {
        'selected_items': selected_items,
        'total_value': total_value,
        'total_weight': total_weight
    }


if __name__ == '__main__':
    uvicorn.run(optimizer, host='localhost', port=8080)
