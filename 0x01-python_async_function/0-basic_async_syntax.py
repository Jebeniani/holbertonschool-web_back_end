#!/usr/bin/python3
"""
asynchronous coroutine that takes in an integer argument named wait_random that
waits for a random delay between 0 and max_delay seconds and eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """_summary_

    Args:
        max_delay (int, optional): _description_. Defaults to 10.

    Returns:
        float: _description_
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
