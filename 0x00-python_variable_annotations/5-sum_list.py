#!/usr/bin/env python3
""" Sum up a list values """


def sum_list(input_list: list) -> float:
    """Sum parameters of the list passed """
    total = 0
    for input in input_list:
        total += input
    return total
