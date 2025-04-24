array=[12,34,55,32,54]
for i in range(0, len(array)):
    print(array[i], end=" ")
    array.append(99)
    array[0]=100
    print("\nArray after modification: ")
    for i in range(0, len(array)):
        print(array[i], end=" ")
  

