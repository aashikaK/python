day="sat"

match day:
    case"mon"|"tues"|"wed"| "thu" | "fri":
        print("WeekDay")
    case "sat" | "sun":
        print("Weekend")


# Using Variables (Capture Values)
match (1, 2):
    case (x, y):
        print(f"x={x}, y={y}")

# Matching with Conditions (Guards)
age=20
match age:
    case a if a<18: #a is a capture variable,It simply means:“Take the value of age and store it in a”
        print("Minor")
    case a if a>=18:
        print("Adult")

# Matching Lists / Tuples
data = [1, 2, 3]

match data:
    case [1, 2, 3]:
        print("Exact match")
    case [1, *rest]:
        print("Starts with 1, rest:", rest)

# Matching Dictionaries
person = {"name": "Alice", "age": 25}

match person:
    case {"name": name, "age": age}: #It is doing pattern matching + capturing values
        print(name, age)

# Default Case (_)
value =0
match value:
    case _:
        print("Anything else")