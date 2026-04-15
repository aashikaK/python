n = [3, 45, 6778, 1, 23, 45, 988, 67]

max_val = max(n)  # just to help logic inside filter

result = filter(lambda x: x == max_val, n)

print(list(result))