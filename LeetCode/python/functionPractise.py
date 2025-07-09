#  Basic Syntax

# def add(a, b):
#     return a + b

# adding data_type hints
# its Optional


# def add(a: int, b: int) -> int:
#     return a + b


# *arugs and **kwargs
def add(*args: int, **kwargs: int) -> int:
    total = 0
    for arg in args:
        total += arg
    for key, value in kwargs.items():
        total += value
    return total


Example usage
result = add(1, 2, 3, x=4, y=5)
print(result)  # Output: 15
