"""custom_random.py"""
from other import func_other
from packA import a1


def func_random(level) -> int:
    """func_random"""
    indent_chars = "  "
    print(f"{indent_chars*level}begin: func_random")
    level += 1
    level = func_other(level)
    level = a1.func_a1(level)
    level -= 1
    print(f"{indent_chars*level}end: func_random")
    return level
