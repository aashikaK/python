import pandas as pd

# Load existing data
df = pd.read_csv('people.csv')

# New row as a dictionary
new_row = {'Name': 'Lumi', 'Age': 3, 'City': 'Cloudland'}

# Append it
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)


# Show updated DataFrame
print(df)
# Filter rows where Age > 20
older_than_20 = df[df['Age'] > 20]

print("\nPeople older than 20:")
print(older_than_20)
