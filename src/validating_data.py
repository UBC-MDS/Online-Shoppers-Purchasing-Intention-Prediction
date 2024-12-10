import pandas as pd
import pandera as pa


def validating_data(onlineshopper_dataframe):
    """
    Validates the input DataFrame against a predefined schema for online shopper data.

    Parameters
    ----------
    onlineshopper_dataframe : pandas.DataFrame
        A DataFrame containing online shopper data to validate. It should be from the UCI Dataset: https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset

    Raises
    ------
    TypeError
        If the input is not a pandas DataFrame.
    ValueError
        If the input DataFrame is empty (contains no rows).
    pandera.errors.SchemaErrors
        If the DataFrame does not conform to the specified schema, including:
        - Missing or mismatched column types.
        - Values outside acceptable ranges.
        - Invalid categorical values.
        - Presence of completely empty rows.

    Schema
    ------
    The DataFrame must satisfy the following constraints:
    - Columns:
        - `Administrative` : int, non-nullable
        - `Administrative_Duration` : float, non-nullable, values between 0 and 86400
        - `Informational` : int, non-nullable
        - `Informational_Duration` : float, non-nullable, values between 0 and 86400
        - `ProductRelated` : int, non-nullable
        - `ProductRelated_Duration` : float, non-nullable, values between 0 and 86400
        - `BounceRates` : float, non-nullable, values between 0 and 1
        - `ExitRates` : float, non-nullable, values between 0 and 1
        - `PageValues` : float, non-nullable
        - `SpecialDay` : float, non-nullable, values between 0 and 1
        - `Month` : str, non-nullable, one of ["Jan", "Feb", "Mar", "Apr", "May", "June", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        - `OperatingSystems` : int, non-nullable
        - `Browser` : int, non-nullable
        - `Region` : int, non-nullable
        - `TrafficType` : int, non-nullable
        - `VisitorType` : str, non-nullable, one of ["New_Visitor", "Returning_Visitor", "Other"]
        - `Weekend` : bool, non-nullable
        - `Revenue` : bool, non-nullable
    - Additional Checks:
        - No completely empty rows are allowed.

    Returns
    -------
    None
        This function performs validation and raises errors for non-compliant DataFrames.
    """
    if not isinstance(onlineshopper_dataframe, pd.DataFrame):
        raise TypeError("Input must be in data type: a pandas DataFrame")    
    if onlineshopper_dataframe.empty:
        raise ValueError("Dataframe cannot be empty, i.e. no rows.")
    
    schema = pa.DataFrameSchema(
        {
            "Administrative": pa.Column(int, nullable=False),
            "Administrative_Duration": pa.Column(float, pa.Check.between(0, 86400), nullable=False),
            "Informational": pa.Column(int, nullable=False),
            "Informational_Duration": pa.Column(float, pa.Check.between(0, 86400), nullable=False),
            "ProductRelated": pa.Column(int, nullable=False),
            "ProductRelated_Duration": pa.Column(float, pa.Check.between(0, 86400), nullable=False),
            "BounceRates": pa.Column(float, pa.Check.between(0, 1), nullable=False),
            "ExitRates": pa.Column(float, pa.Check.between(0, 1), nullable=False),
            "PageValues": pa.Column(float, nullable=False),
            "SpecialDay": pa.Column(float, pa.Check.between(0, 1), nullable=False),
            "Month": pa.Column(str, pa.Check.isin(["Jan", "Feb", "Mar", "Apr", "May", "June", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]), nullable=False),
            "OperatingSystems": pa.Column(int, nullable=False),
            "Browser": pa.Column(int, nullable=False),
            "Region": pa.Column(int, nullable=False),
            "TrafficType": pa.Column(int, nullable=False), 
            "VisitorType": pa.Column(str, pa.Check.isin(["New_Visitor", "Returning_Visitor", "Other"]), nullable=False),
            "Weekend": pa.Column(bool, nullable=False),
            "Revenue": pa.Column(bool, nullable=False),
        },
        checks=[
            pa.Check(lambda dfpa: ~(dfpa.isna().all(axis=1)).any(), error="Empty rows found.")
        ]
    )
    
    schema.validate(onlineshopper_dataframe, lazy=True)