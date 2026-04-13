# Function type hints tell what type of input a function should take and what type it will return.
# They are used using : and ->.

def add(a:int,b:int)->int:
    return a+b

print(add(5,6))

# Type hints are NOT enforced in Python
def add(a: int, b: int) -> int:
    return a + b

print(add("2", "3"))  # still runs! but returns 23 not 5