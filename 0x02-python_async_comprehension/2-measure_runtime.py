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
    start_time = time.time()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()

    return (end_time - start_time)
