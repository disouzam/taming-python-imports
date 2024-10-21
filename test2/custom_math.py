"""custom_math.py"""
from custom_random import func_random
from packA.a1 import func_a1


def func_math(level) -> int:
    """func_math"""
    indent_chars = "  "
    print(f"{indent_chars*level}begin: func_math")
    level += 1
    level = func_random(level)
    level = func_a1(level)
    level -= 1
    print(f"{indent_chars*level}end: func_math")
    return level
