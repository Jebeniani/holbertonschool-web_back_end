#!/usr/bin/env python3
"""
function "sum_list" which takes a list "input_list" of floats
as argument and returns their sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """_summary_

    Args:
        input_list (List[float]): _description_

    Returns:
        float: _description_
    """
    return sum(input_list)
