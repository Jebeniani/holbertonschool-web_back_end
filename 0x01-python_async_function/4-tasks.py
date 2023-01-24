#!/usr/bin/env python3
"""
same but different
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """_summary_

    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
        List[float]: _description_
    """
    tasks = []
    for i in range(n):
        tasks.append(task_wait_random(max_delay))
    delays = [await task for task in tasks]
    delays.sort()
    return delays
