#!/usr/bin/env python3
"""_summary_

    Returns:
        _type_: _description_
    """


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """_summary_

    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
        List[float]: _description_
    """
    delays = []
    for i in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    delays.sort()
    return delays
