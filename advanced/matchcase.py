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