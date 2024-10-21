"""other.py"""


def func_other(level) -> int:
    """func_other"""
    indent_chars = "  "
    print(f"{indent_chars*level}begin: func_other")
    level += 1
    level -= 1
    print(f"{indent_chars*level}end: func_other")
    return level
