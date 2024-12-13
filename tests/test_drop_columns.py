import pandas as pd
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.drop_columns import drop_columns

# proper input data
df_1 = pd.DataFrame({
    'jack_fruit': [0, 1, 2, 3],
    'durian': [4, 5, 6, 7],
    'lychee': [8, 9, 10, 11],
    'pomelo': [12, 13, 14, 15]
})
df_2 = pd.DataFrame({
    'jack_fruit': [0, 1, 2, 3],
    'durian': [4, 5, 6, 7],
    'mangosteen': [8, 9, 10, 11],
    'kumquat': [12, 13, 14, 15]
})
df_1_small = pd.DataFrame({
    'jack_fruit': [0, 1, 2, 3],
    'durian': [4, 5, 6, 7]
})
df_2_small = pd.DataFrame({
    'jack_fruit': [0, 1, 2, 3],
    'durian': [4, 5, 6, 7]
})
columns_to_drop_1 = ['durian']
columns_to_drop_2 = ['jack_fruit', 'durian']

# inproper input data
empty_list = []
string_not_list = "hello!"
list_no_dfs = [30, "hello!"]
list_dfs_with_integer = [df_1, df_2, 30]
list_dfs_with_string = [df_1, "hello!", df_2]
nested_dataframe_list = [[df_1, df_2], [df_1_small], df_2_small]

# expected outputs
df_1_drop_1 = pd.DataFrame({
    'jack_fruit': [0, 1, 2, 3],
    'lychee': [8, 9, 10, 11],
    'pomelo': [12, 13, 14, 15]
})
df_2_drop_1 = pd.DataFrame({
    'jack_fruit': [0, 1, 2, 3],
    'mangosteen': [8, 9, 10, 11],
    'kumquat': [12, 13, 14, 15]
})
df_1_drop_2 = pd.DataFrame({
    'lychee': [8, 9, 10, 11],
    'pomelo': [12, 13, 14, 15]
})
df_2_drop_2 = pd.DataFrame({
    'mangosteen': [8, 9, 10, 11],
    'kumquat': [12, 13, 14, 15]
})

# tests

# expected cases
def drop_2_columns_success():
    """
    `drop_columns` should return the list of the inputted pandas dataframes,
    but with the specified columns dropped (list_of_columns). In this test,
    the two specified columns should be dropped.
    This test checks if:
    - the result is the expected list dataframes with the columns dropped
    - the result is a list
    - if each element in the result is a pandas.DataFrame
    """
    result = drop_columns([df_1, df_2], columns_to_drop_1)
    assert result.equals([df_1_drop_1, df_2_drop_1])
    assert isinstance(result, list)
    assert all(isinstance(df, pd.DataFrame) for df in result)

def drop_1_columns_success():
    """
    `drop_columns` should return the list of the inputted pandas dataframes,
    but with the specified columns dropped (list_of_columns). In this test,
    the one specified column should be dropped.
    This test checks if:
    - the result is the expected list dataframes with the columns dropped
    - the result is a list
    - if each element in the result is a pandas.DataFrame
    """
    result = drop_columns([df_1, df_2], columns_to_drop_2)
    assert result.equals([df_1_drop_2, df_2_drop_2])
    assert isinstance(result, list)
    assert all(isinstance(df, pd.DataFrame) for df in result)

def drop_no_columns_success():
    """
    `drop_columns` should return the list of the inputted pandas dataframes,
    but with the specified columns dropped (list_of_columns). In this test, 
    no columns should be dropped since an empty list is inputted for list_of_columns
    and a warning should be given.
    """
# test for returning the unchanged input dataframes when list_of_columns is an empty list
# empty list


# edge cases
# return empty dataframe(s) when all columns are dropped
# for i in range(0, len(resulting_dataframes)):
# assert df[i].empty


# test for raising a type error when list_of_dataframes is not a list of pandas dataframes
# empty list
# a string, not a list
# list with dataframes, except one integer
# list with dataframes, except one string
# a nested list of dataframes


# test for raising a type error when list_of_columns is not a list of strings.
# list with an integer and boolean
# list with strings, except one integer
# list with strings, except one boolean
# a nested list of strings

# test for raising a warning when list_of_columns is an empty list
# empty list

# test for returning the unchanged input dataframes when list_of_columns is an empty list
# empty list

# test for raising a key error if any element of list_of_columns is not a column in any element of list_of_dataframes
# 