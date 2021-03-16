from typing import List

from pydantic import BaseModel

from schema.item import Item


class Knapsack(BaseModel):
    """Class to validate the knapsack model"""

    items: List[Item]
    capacity: float
