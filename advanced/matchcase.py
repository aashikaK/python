day="sat"

match day:
    case"mon"|"tues"|"wed"| "thu" | "fri":
        print("WeekDay")
    case "sat" | "sun":
        print("Weekend")