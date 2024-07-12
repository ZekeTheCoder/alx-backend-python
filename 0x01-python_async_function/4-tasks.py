#!/usr/bin/env python3
"""
Module that defines task_wait_n function using task_wait_random.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that waits for random delays using task_wait_random.
    """
    delays: List[float] = []
    all_delays: List[float] = []

    for num in range(n):
        delays.append(task_wait_random(max_delay))

    for delay in asyncio.as_completed(delays):
        result = await delay
        all_delays.append(result)

    return (all_delays)
