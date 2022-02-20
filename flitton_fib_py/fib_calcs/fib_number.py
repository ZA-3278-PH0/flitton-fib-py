import imp
from typing import Optional

def recurring_fibonacci_number(number: int) -> Optional[int]:
    if number < 0:
        raise ValueError("Fibonacci has to be equal or above zero")
    elif number <= 1:
        return number
    else:
        return recurring_fibonacci_number(number - 1) + \
                recurring_fibonacci_number(number - 2)

# trigger build (14-6-2021)                