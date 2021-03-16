from dataclasses import dataclass

import numpy as np


@dataclass
class Problem:
    """Class that represents the 'business' knapsack problem"""

    capacity: float
    names: np.ndarray
    weights: np.ndarray
    values: np.ndarray
