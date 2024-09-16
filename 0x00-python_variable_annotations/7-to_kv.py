#!/usr/bin/env python3
""" Complex conversion """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Complex conversion function """
    return (k, float(v ** 2))
