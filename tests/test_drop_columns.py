sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.drop_columns import drop_columns

# tests

# expected cases

# edge cases
# return empty dataframe(s) when all columns are dropped


# test for raising a type error when list_of_dataframes is not a list of pandas dataframes
# empty list
# list with an integer, string, and boolean
# list with dataframes, except one integer
# list with dataframes, except one string
# list with dataframes, except one boolean
# a nested list of dataframes


# test for raising a type error when list_of_columns is not a list of strings.
# list with an integer and boolean
# list with strings, except one integer
# list with strings, except one boolean
# a nested list of strings

# test for raising a key error if any element of list_of_columns is not a column in any element of list_of_dataframes
# 

# test for raising a warning when list_of_columns is an empty list
# empty list

# test for returning the unchanged input dataframes when list_of_columns is an empty list
# empty list

# test for key error when any element of list_of_columns is not a column in any element of list_of_dataframes.