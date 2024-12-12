import os

def create_X_and_y_splits_and_save(train_df, test_df, target_column, data_to):
    """
    Saves pre-split training and testing datasets for features and target as CSV files.

    Parameters:
    ----------
    train_df : pandas.DataFrame
        The training dataset.
    test_df : pandas.DataFrame
        The testing dataset.
    target_column : str
        The column name to be used as the target (y).
    data_to : str
        The path to the directory where the CSV files will be saved.

    Returns:
    -------
    None

    Raises:
    -------
    ValueError
        If either the training or test DataFrames is empty.
    KeyError
        If the target column is not found in either the training or test DataFrames.
    OSError
        If the output directory cannot be created because of invalid path.
    
    """

    # Check for empty DataFrames, other wise throw error
    if train_df.empty or test_df.empty:
        raise ValueError("Input DataFrames cannot be empty.")

    # Make sure the target column exists, otherwise throw error
    if target_column not in train_df.columns or target_column not in test_df.columns:
        raise KeyError(f"Target column '{target_column}' not found in the DataFrames.")
    
    # ensure the output directory exists
    os.makedirs(data_to, exist_ok=True)

    # create X and y train/test sets from target_column
    X_train = train_df.drop(columns=[target_column])
    y_train = train_df[target_column]
    X_test = test_df.drop(columns=[target_column])
    y_test = test_df[target_column]

    # save datasets to the directory input
    X_train.to_csv(os.path.join(data_to, "X_train.csv"), index=False)
    y_train.to_csv(os.path.join(data_to, "y_train.csv"), index=False)
    X_test.to_csv(os.path.join(data_to, "X_test.csv"), index=False)
    y_test.to_csv(os.path.join(data_to, "y_test.csv"), index=False)
