#!/usr/bin/env python3
"""
Module to define task_wait_random function that returns asyncio.Task.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular function that returns an asyncio.Task for wait_random(max_delay).
    """
    async_task = asyncio.create_task(wait_random(max_delay))

    return async_task
