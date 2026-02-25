n=int(input('Enter the number whose multiplication table you want to print in reverse order: '))

for i in range(1,11):
    print(f'{n} X {11-i} = {n*(11-i)}')