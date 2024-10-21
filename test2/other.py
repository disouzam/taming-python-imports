"""other.py"""


def func_other(level) -> int:
    """func_other"""
    tabChar = "  "
    print(f"{tabChar*level}begin: func_other")
    level += 1
    level -= 1
    print(f"{tabChar*level}end: func_other")
    return level
