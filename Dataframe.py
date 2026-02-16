import pandas as pd

# DataFrame = A tabular data structure with rows AND columns (2 Dimensional)
#             Similar to an excel spreadsheet

data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50]
}

df = pd.DataFrame(data)
df2 = pd.DataFrame(data, index = ["Employee 1", "Employee 2", "Employee 3"])

print(df2) 

# acess specific row
print(df2.loc["Employee 2"])
# Using intricate(default) location
print(df2.iloc[1])

# Add a new column
df2["Job"] = ["Cook", "NA", "Cashier"]

# Add a new rows
new_rows = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"}, 
                         {"Name": "Manvi", "Age": 19, "Job": "Student"}], 
                         index = ["Employee 4", "Employee 5"])
df2 = pd.concat([df2 , new_rows])
print(df2)