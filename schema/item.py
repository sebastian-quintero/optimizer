from pydantic import BaseModel


class Item(BaseModel):
    """Class to validate an item of the knapsack"""

    name: str
    weight: float
    value: float
