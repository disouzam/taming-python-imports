"""start.py"""
from custom_math import func_math
from custom_random import func_random


def main(level) -> int:
    """Entry point"""
    level += 1
    level = func_math(level)
    level = func_random(level)
    return level


if __name__ == '__main__':
    level = 0
    main(level)
    print(f"Level: {level}")
