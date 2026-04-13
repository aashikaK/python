# so that program doesnot crash 

try:
    age = -5
    if age < 0:
        raise ValueError("Invalid age")

except ValueError as e:
    print("Handled:", e)