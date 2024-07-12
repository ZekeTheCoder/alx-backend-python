#!/usr/bin/env python3
"""
Module that returns the list of all delays (float values).
"""

from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and
    returns the list of all the delays in ascending order.
    """
    delays: List[float] = []
    all_delays: List[float] = []

    # Spawn wait_random n times and append the coroutines to the delays list
    for _ in range(n):  # '_' means variable is intentionally not used
        delays.append(wait_random(max_delay))

    # Process the completed coroutines as they finish
    for delay in asyncio.as_completed(delays):
        res = await delay
        all_delays.append(res)

    return all_delays
