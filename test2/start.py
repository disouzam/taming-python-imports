"""start.py"""
from custom_math import func_math
from custom_random import func_random
from packA.a1 import func_a1


def main(level) -> int:
    """Entry point"""
    level += 1
    level = func_math(level)
    level = func_random(level)
    level = func_a1(level)
    return level


if __name__ == '__main__':
    level = 0
    main(level)
    print(f"Level: {level}")
