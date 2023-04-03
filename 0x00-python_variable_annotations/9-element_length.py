#!/usr/bin/env python3
"""Module: iterable object"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Element Length"""
    return [(i, len(i)) for i in lst]
