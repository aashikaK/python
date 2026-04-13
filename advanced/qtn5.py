try:
    n=int(input("Enter a number: "))
except ValueError as v:
    print(v)

else:
    multiplication=[i*n for i in range(1,11)]
    print(multiplication)

    try:
        with open("advanced/table.txt","a") as f:
            f.write(f"\nMultiplications of {n}: {multiplication}")
            print("Printed successfully in 'table.txt'.")

    except FileNotFoundError:
        print("The file doesnot exit")
