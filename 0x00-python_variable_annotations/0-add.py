#!/usr/bin/env python3
""" Type annotated add function """


def add(a: float, b: float) -> float:
    """ A function that adds two numbers passed as arg,
        the args was typed annotated, throws err if:
        other type is passed
        return:
            a + b
    """
    return a + b