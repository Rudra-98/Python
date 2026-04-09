import numpy as np
import pandas as pd


dict = {
    'names':['chandu','nikitha','yadav'],
    'age':[27,25,100],
    'location':['hyderabad','bangalore','nizambad']
}


dict_df = pd.DataFrame(dict)


print(dict_df)
#
# loc → Label-based indexing
# Uses row/column labels (names)
# Includes the end index when slicing
# Works with index names and column names

print(dict_df.loc[0])


print(dict_df.loc[1,'age'])

print(type(dict_df.loc[1]))

# iloc → Position-based indexing
# Uses integer positions (0, 1, 2...)
# Excludes the end index (like Python slicing)
# Works like standard list indexing


print(dict_df.iloc[0])


# print(dict_df[1:2])

# print(dict_df.iloc[1:2,:])

# 1: → start from 1th row (because indexing starts at 0)
# : → select all columns
# Goes till the end of the DataFrame

print(dict_df.iloc[1:,:])

print(dict_df.describe())