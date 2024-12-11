import pytest
import os
import numpy as np
import pandas as pd
import pandera as pa
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.validating_data import validating_data

# Test data setup
valid_data = pd.DataFrame({
    "Administrative": [1, 2],
    "Administrative_Duration": [100.0, 200.0],
    "Informational": [0, 1],
    "Informational_Duration": [50.0, 150.0],
    "ProductRelated": [10, 20],
    "ProductRelated_Duration": [300.0, 600.0],
    "BounceRates": [0.1, 0.2],
    "ExitRates": [0.3, 0.4],
    "PageValues": [0.0, 100.0],
    "SpecialDay": [0.0, 0.8],
    "Month": ["Jan", "Feb"],
    "OperatingSystems": [1, 2],
    "Browser": [1, 2],
    "Region": [1, 2],
    "TrafficType": [1, 2],
    "VisitorType": ["New_Visitor", "Returning_Visitor"],
    "Weekend": [True, False],
    "Revenue": [False, True],
})

invalid_data_type = []
empty_data = pd.DataFrame()
missing_columns_data = pd.DataFrame({
    "Administrative": [1],
    "Administrative_Duration": [100.0]
})
invalid_categorical_values = pd.DataFrame({
    "Administrative": [1],
    "Administrative_Duration": [100.0],
    "Informational": [0],
    "Informational_Duration": [50.0],
    "ProductRelated": [10],
    "ProductRelated_Duration": [300.0],
    "BounceRates": [0.1],
    "ExitRates": [0.3],
    "PageValues": [0.0],
    "SpecialDay": [0.0],
    "Month": ["InvalidMonth"],
    "OperatingSystems": [1],
    "Browser": [1],
    "Region": [1],
    "TrafficType": [1],
    "VisitorType": ["InvalidVisitor"],
    "Weekend": [True],
    "Revenue": [False],
})

# Test a valid DataFrame passes validation.
def test_valid_dataframe():
    validating_data(valid_data)

# Test input is not a pandas DataFrame.
def test_invalid_type():
    with pytest.raises(TypeError, match="Input must be in data type: a pandas DataFrame"):
        validating_data(invalid_data_type)
        
# Test an empty DataFrame.
def test_empty_dataframe():
    with pytest.raises(ValueError, match="Dataframe cannot be empty, i.e. no rows."):
        validating_data(empty_data)

# Test DataFrame with missing required columns.
def test_missing_columns():
    with pytest.raises(pa_errors.SchemaError):
        validating_data(missing_columns_data)

# Test DataFrame with invalid categorical values.
def test_invalid_categorical_values():
    with pytest.raises(pa_errors.SchemaError):
        validating_data(invalid_categorical_values)