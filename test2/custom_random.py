"""custom_random.py"""
from other import func_other


def func_random(level) -> int:
    """func_random"""
    tabChar = "  "
    print(f"{tabChar*level}begin: func_random")
    level += 1
    level = func_other(level)
    level -= 1
    print(f"{tabChar*level}end: func_random")
    return level
