from typing import Union
def increment(value : int, cap : int, step : int = "1") -> int:
    if value < cap:
        return value + step
    return value

print(increment(9, 10, 1))
print(increment(10, 10))
print(increment("8", "9"))
print(increment(9, 10))
