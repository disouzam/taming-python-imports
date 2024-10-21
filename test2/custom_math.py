"""custom_math.py"""
from custom_random import func_random


def func_math(level) -> int:
    """func_math"""
    tabChar = "  "
    print(f"{tabChar*level}begin: func_math")
    level += 1
    level = func_random(level)
    level -= 1
    print(f"{tabChar*level}end: func_math")
    return level
