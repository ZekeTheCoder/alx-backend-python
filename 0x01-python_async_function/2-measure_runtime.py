#!/usr/bin/env python3
"""
Module to measure the average execution time of wait_n function.
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time of wait_n(n, max_delay).
    """
    start_time = time.time()
    # Run wait_n(n, max_delay) and measure total elapsed time
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    time_elapsed = end_time - start_time

    return (time_elapsed / n)
