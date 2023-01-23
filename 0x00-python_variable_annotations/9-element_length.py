#!/usr/bin/env python3
"""
element length
"""
from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """_summary_

    Args:
        lst (Iterable[Sequence]): _description_

    Returns:
        List[Tuple[Sequence, int]]: _description_
    """
    return [(i, len(i)) for i in lst]
