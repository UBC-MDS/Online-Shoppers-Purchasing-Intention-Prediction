import os
import pandas as pd
import pytest
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.create_X_and_y_splits_and_save import create_X_and_y_splits_and_save



# sample train data inputs
train_data = pd.DataFrame({
        "Feature1": [1, 2, 3],
        "Feature2": [10, 20, 30],
        "Target": [0, 1, 0]})

# Sample test data inputs
test_data = pd.DataFrame({
        "Feature1": [4, 5],
        "Feature2": [40, 50],
        "Target": [1, 0]
    })

# Expected test outputs
expected_X_train = pd.DataFrame({"Feature1": [1, 2, 3], "Feature2": [10, 20, 30]})
expected_y_train = pd.DataFrame({"Target": [0, 1, 0]})
expected_X_test = pd.DataFrame({"Feature1": [4, 5], "Feature2": [40, 50]})
expected_y_test = pd.DataFrame({"Target": [1, 0]})

# Empty DataFrame inputs
empty_train_data = pd.DataFrame({"Feature1": [], "Feature2": [], "Target": []})
empty_test_data = pd.DataFrame({"Feature1": [], "Feature2": [], "Target": []})


# `create_X_and_y_split_and_save` should take in train and test df, along with the target column
# name and then make the X and y train and test data. It should then save the X and y train/test
# dataframes to the directory

def test_save_data_splits_success(tmpdir):
    output_dir = tmpdir.mkdir("output")

    # Run the function
    create_X_and_y_splits_and_save(train_data, test_data, "Target", output_dir)

    # Check if the files exist
    assert os.path.exists(os.path.join(output_dir, "X_train.csv"))
    assert os.path.exists(os.path.join(output_dir, "y_train.csv"))
    assert os.path.exists(os.path.join(output_dir, "X_test.csv"))
    assert os.path.exists(os.path.join(output_dir, "y_test.csv"))

    # Load the outputs
    X_train = pd.read_csv(os.path.join(output_dir, "X_train.csv"))
    y_train = pd.read_csv(os.path.join(output_dir, "y_train.csv"))
    X_test = pd.read_csv(os.path.join(output_dir, "X_test.csv"))
    y_test = pd.read_csv(os.path.join(output_dir, "y_test.csv"))

    # Validate contents
    assert X_train.equals(expected_X_train)
    assert y_train.equals(expected_y_train)
    assert X_test.equals(expected_X_test)
    assert y_test.equals(expected_y_test)


# Test edge cases
def test_save_data_splits_empty():
    with pytest.raises(ValueError):
        create_X_and_y_splits_and_save(empty_train_data, empty_test_data, "Target", "dummy_dir")


# Test invalid arguments
def test_save_data_splits_errors():
    # Invalid target column
    with pytest.raises(KeyError):
        create_X_and_y_splits_and_save(train_data, test_data, "InvalidColumn", "dummy_dir")

    # Invalid directory path
    with pytest.raises(OSError):
        create_X_and_y_splits_and_save(train_data, test_data, "Target", "/invalid/path")
