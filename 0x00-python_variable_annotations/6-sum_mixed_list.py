#!/usr/bin/env python3
""" Sum up a mixed list values """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum parameters of the mixed list passed """
    total = 0
    for index in mxd_lst:
        total += index
    return total
