import pandas as pd

def drop_columns(list_of_dataframes, list_of_columns):
    """
    Returns the list of dataframes with the columns dropped.

    Parameters
    ----------
    list_of_dataframes : list of pandas.DataFrames
        A list of dataframes to drop columns from.
    list_of_columns : list of str
        A list of column names to be dropped from the dataframes.

    Raises
    ------
    TypeError:
        If list_of_dataframes is not a list of pandas dataframes.
        If list_of_columns is not a list of strings.
    KeyError:
        If any element of list_of_columns is not a column in any element of list_of_dataframes.

    Returns
    -------
    list of pandas.DataFrames
        The resulting dataframes after dropping the specified columns.

    Example
    -------
    >>> df_1 = pd.DataFrame({
    ...    'jack_fruit': [0, 1, 2, 3],
    ...    'durian': [4, 5, 6, 7],
    ...    'lychee': [8, 9, 10, 11],
    ...    'pomelo': [12, 13, 14, 15]
    ... })
    >>> df_2 = pd.DataFrame({
    ...    'jack_fruit': [0, 1, 2, 3],
    ...    'durian': [4, 5, 6, 7],
    ...    'mangosteen': [8, 9, 10, 11],
    ...    'kumquat': [12, 13, 14, 15]
    ... })
    >>> df_1, df_2 = drop_columns([df_1, df_2], ['jack_fruit', 'durian'])
    >>> df_1
        lychee    pomelo
    0    8          12
    1    9          13
    2    10         14
    3    11         15

    >>> df 2
        mangosteen    kumquat
    0    8              12
    1    9              13
    2    10             14
    3    11             15
    """