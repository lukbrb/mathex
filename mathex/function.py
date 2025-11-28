"""Module defining mathematical functions and their implementations."""

import math
from typing import Callable, Dict

# Dictionary mapping function names to their implementations
FUNCTIONS: Dict[str, Callable[[float], float]] = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "exp": math.exp,
    "sqrt": math.sqrt,
    # Add more functions as needed
}
