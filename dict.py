my_dict = {
    "name": "Aashika",
    "age": 21,
    "city": "Kathmandu"
}
print(my_dict["name"])  # Output: Aashika
my_dict["age"] = 22
my_dict["hobby"] = "Coding"
del my_dict["city"]
for key, value in my_dict.items():
    print(key, "=>", value)
