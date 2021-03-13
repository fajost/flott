import logging

from services.logging import init_logging


def example_sum(num1: int, num2: int) -> int:
    init_logging()
    result = num1 + num2
    logging.debug(f"Calculated sum of {num1} and {num2} as {result}")
    return result


if __name__ == "__main__":
    example_sum(2, 3)
