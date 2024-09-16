#!/usr/bin/env python3
""" Sum up a list values """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum parameters of the list passed """
    total = 0
    for input in input_list:
        total += input
    return total
