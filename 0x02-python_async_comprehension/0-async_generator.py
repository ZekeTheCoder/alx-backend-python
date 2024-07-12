#!/usr/bin/env python3
"""
This module defines an asynchronous generator function that yields random
numbers after waiting asynchronously for 1 second on each iteration.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator function that yields random numbers.
    """

    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
