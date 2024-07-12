#!/usr/bin/env python3
"""
Module that measures the runtime for executing async_comprehension
four times in parallel.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the runtime for executing
    async_comprehension four times in parallel.
    """
    tasks = []

    start_time = time.time()

    # Execute async_comprehension four times in parallel
    for num in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))

    await asyncio.gather(*tasks)

    end_time = time.time()
    total_runtime = end_time - start_time

    return total_runtime
