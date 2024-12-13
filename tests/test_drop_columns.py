import pandas as pd
import pytest
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

# improper input for list_of_dataframes
empty_list = []
string_not_list = "hello!"
list_no_dfs = [30, "hello!"]
list_dfs_with_integer = [df_1, df_2, 30]
list_dfs_with_string = [df_1, "hello!", df_2]
nested_dataframe_list = [[df_1, df_2], [df_1_small], df_2_small]

# improper types of input for list_of_columns
list_int_bool = [0, True]
list_str_with_integer = ['hello!', 6, 'wow']
list_str_with_bool = ['hello!', 'wow', False]
list_str_nested = [['hello!', 'wow'], 'hello!', ['wow']]

# improper input for list_of_columns (not a column in one or all of list_of_dataframes)
one_elem_not_in_any = ['jack_fruit', 'durian', 'huh?']
one_elem_not_in_one = ['jack_fruit', 'durian', 'mangosteen']
any_elem_not_in_any = ['huh?', "that's weird"]
any_elem_not_in_one = ['lychee', 'pomelo']

# tests

# expected cases
def test_drop_2_columns_success():
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
    expected_result = [df_1_drop_1, df_2_drop_1]
    assert all(result[i].equals(expected_result[i]) for i in range(0, len(result)))
    assert isinstance(result, list)
    assert all(isinstance(df, pd.DataFrame) for df in result)

def test_drop_1_columns_success():
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
    expected_result = [df_1_drop_2, df_2_drop_2]
    assert all(result[i].equals(expected_result[i]) for i in range(0, len(result)))
    assert isinstance(result, list)
    assert all(isinstance(df, pd.DataFrame) for df in result)

# edge cases
def test_drop_no_columns_success():
    """
    `drop_columns` should return the list of the inputted pandas dataframes,
    but with the specified columns dropped (list_of_columns). In this test, 
    no columns should be dropped since an empty list is inputted for list_of_columns
    and a UserWarning should be given.
    This test checks if:
    - if a UserWarning is given
    - the result is the same as the inputted list of dataframes
    - the result is a list
    - if each element in the result is a pandas.DataFrame
    """
    with pytest.warns(UserWarning, match = "list_of_columns is an empty list. Unchanged list_of_dataframes returned."):
        result = drop_columns([df_1, df_2], [])
        expected_result = [df_1, df_2]
        assert all(result[i].equals(expected_result[i]) for i in range(0, len(result)))
        assert isinstance(result, list)
        assert all(isinstance(df, pd.DataFrame) for df in result)

def test_drop_all_columns_success():
    """
    `drop_columns` should return the list of the inputted pandas dataframes,
    but with the specified columns dropped (list_of_columns). In this test,
    the specified columns should be dropped, causing the result to be a list
    of empty dataframes.
    This test checks if:
    - if each element in the result is an empty pandas.DataFrame
    - the result is a list
    - if each element in the result is a pandas.DataFrame
    """
    result = drop_columns([df_1_small, df_2_small], columns_to_drop_2)
    assert all(df.empty for df in result)
    assert isinstance(result, list)
    assert all(isinstance(df, pd.DataFrame) for df in result)

# error cases
def test_drop_columns_error_not_df_list():
    """
    `drop_columns` should raise a TypeError when the inputted list_of_dataframes
    is not a list of pandas dataframes.
    This test checks if a TypeError is raised when the inputted list_of_dataframes is:
    - an empty list
    - a string, not a list
    - list with pandas dataframes, except one integer
    - list with pandas dataframes, except one string
    - nested list of dataframes
    """
    with pytest.raises(TypeError, match="list_of_dataframes must be a list of pandas DataFrames."):
        drop_columns(empty_list, columns_to_drop_2)
        drop_columns(string_not_list, columns_to_drop_2)
        drop_columns(list_no_dfs, columns_to_drop_2)
        drop_columns(list_dfs_with_integer, columns_to_drop_2)
        drop_columns(list_dfs_with_string, columns_to_drop_2)
        drop_columns(nested_dataframe_list, columns_to_drop_2)

def test_drop_columns_error_not_col_string_list():
    """
    `drop_columns` should raise a TypeError when the inputted list_of_columns
    is not a list of strings.
    This test checks if a TypeError is raised when the inputted list_of_dataframes is:
    - list with an integer and boolean
    - a string, not a list
    - list with strings, except one integer
    - list with strings, except one boolean
    - a nested list of strings
    """
    with pytest.raises(TypeError, match="list_of_columns must be a list of strings."):
        drop_columns([df_1, df_2], list_int_bool)
        drop_columns([df_1, df_2], list_str_with_integer)
        drop_columns([df_1, df_2], list_str_with_bool)
        drop_columns([df_1, df_2], list_str_nested)

def test_drop_columns_col_not_found():
    """
    `drop_columns` should raise a KeyError when any element of list_of_columns
    is not a column in any dataframe in list_of_dataframes.
    This test checks if a KeyError is raised when:
    - one of the elements of list_of_columns isn't a column in any of the dataframes in list_of_dataframes
    - one of the elements of list_of_columns isn't a column in one of the dataframes in list_of_dataframes
    - all the elements of list_of_columns isn't a column in any of the dataframes in list_of_dataframes
    - all the elements of list_of_columns isn't a column in one of the dataframes in list_of_dataframes
    """
    with pytest.raises(KeyError):
        drop_columns([df_1, df_2], one_elem_not_in_any)
        drop_columns([df_1, df_2], one_elem_not_in_one)
        drop_columns([df_1, df_2], any_elem_not_in_any)
        drop_columns([df_1, df_2], any_elem_not_in_one)