import pandas as pd

#Series = A pandas 1-Dimensional arrray which can store any type of data
#       Think of it as 1 Column in a spreadsheet

data = [100, 102, 104, 200, 204]

series = pd.Series(data)
# To set any value of index
series2 = pd.Series(data, index = ["a", "b", "c", "d", "e"])

print(series)
print(series2)

# To print value at a particular index(label)
print(series2.loc["b"])

# Printing value using intricate(default) index
print(series2.iloc[0])

# To filter values eg: greater than or equal to 200
print(series2[series2 >= 200])

calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}
seriesC = pd.Series(calories)

print(seriesC)