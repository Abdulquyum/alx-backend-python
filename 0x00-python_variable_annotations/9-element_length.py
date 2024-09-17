#!/usr/bin/env python3
""" Annotated function that returns fumction """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' Outisde Multiplier function '''
    def inner_multiplier(value: float) -> float:
        ''' Multiply float by multiplier '''
        return value * multiplier
    return inner_ multiplier
