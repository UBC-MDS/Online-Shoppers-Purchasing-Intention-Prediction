import pandas as pd
import warnings

def drop_columns(list_of_dataframes, list_of_columns):
    """
    Returns the list of dataframes with the columns dropped.

    Parameters
    ----------
    list_of_dataframes : list of pandas.DataFrames
        A list of dataframes to drop columns from.
    list_of_columns : list of str
        A list of column names to be dropped from the dataframes.

    Warnings
    --------
    UserWarning:
        If `list_of_columns` is an empty list. An unchanged list_of_dataframes will be returned.

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
    # check if list_of_dataframes is a list of pandas dataframes
    if not isinstance(list_of_dataframes, list) or not all(isinstance(df, pd.DataFrame) for df in list_of_dataframes):
        raise TypeError("list_of_dataframes must be a list of pandas DataFrames.")

    # check if list_of_columns is empty (early return with unchanged input dfs)
    if len(list_of_columns) == 0:
        warnings.warn("list_of_columns is an empty list. Unchanged list_of_dataframes returned.")
        return list_of_dataframes
    
    # check if list_of_columns is a list of strings
    if not isinstance(list_of_columns, list) or not all(isinstance(col, str) for col in list_of_columns):
        raise TypeError("list_of_columns must be a list of strings.")

    # check if any element of list_of_columns is not a column in any element of list_of_dataframes
    for i, dataframe in enumerate(list_of_dataframes):
        for column in list_of_columns:
            if column not in dataframe.columns.to_list():
                raise KeyError(f"DataFrame at index {i} of list_of_dataframes does not have a column named '{column}'.")

    # drop columns if they exist in each dataframe of list_of_dataframes
    list_dataframes_without_cols = []
    for dataframe in list_of_dataframes:
        dataframe_without_col = dataframe.drop(columns=list_of_columns)
        list_dataframes_without_cols.append(dataframe_without_col)
    return list_dataframes_without_cols