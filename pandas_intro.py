# import pandas as pd

# # Creating a simple data table (DataFrame)
# data = {
#     'Name': ['Aashika', 'Samy', 'Chatu'],
#     'Age': [21, 22, 19],
#     'City': ['Kathmandu', 'Pokhara', 'Internet']
# }

# df = pd.DataFrame(data)

# # Display the DataFrame
# print(df)
import pandas as pd

# Reading the CSV file
df = pd.read_csv('people.csv')

# Show the full data
print("Full Data:")
print(df)

# Show just names
print("\nNames only:")
print(df['Name'])

