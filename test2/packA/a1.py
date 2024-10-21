"""a1.py"""


def func_a1(level) -> int:
    """func_a1"""
    indent_chars = "  "
    print(f"{indent_chars*level}begin: func_a1")
    level += 1
    level -= 1
    print(f"{indent_chars*level}end: func_a1")
    return level
