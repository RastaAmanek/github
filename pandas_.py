import pandas as pd
import numpy as np

array_ = np.array([1, 2, 3, 4, 5])
print(pd.Series([1, 2, 3, 4, 5]))

my_dict = {"a": [12, 23, 34], "b": [45, 56, 67]}
my_df = pd.DataFrame(my_dict, index=[1, 2, 3])
print(my_df)

print(my_df.values)

df = pd.read_csv("cars.csv")
print(df)
