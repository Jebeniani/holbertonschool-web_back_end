#!/usr/bin/env python3
"""
a type-annotated function make_multiplier that takes
a float multiplier as argument and returns
a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """_summary_

    Args:
        multiplier (float): _description_

    Returns:
        Callable[[float], float]: _description_
    """
    def multiply_by_multiplier(x: float) -> float:
        return x * multiplier
    return multiply_by_multiplier
