# extract_data.py
# Author: Julian Daduica
# Date: 2024-12-03

# This script gets the "Online Shoppers Purchasing Intention Dataset" from the UCI ML repository,
# saves it as a CSV file, and validates the data schema.
#
# Usage: python scripts/01_extract_data.py \
# --write_to=data/raw/



from ucimlrepo import fetch_ucirepo # raw data is from this package
import click
import os
import requests
import pandas as pd
import pandera as pa
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.validating_data import validating_data



def check_directory_exists(directory):
    if not os.path.isdir(directory):
        raise ValueError('The directory provided does not exist.')


@click.command()
@click.option('--write_to', type = str, help = "Path to directory where raw data will be written to")
def main(write_to):

    """
    Fetches the "Online Shoppers Purchasing Intention Dataset" from the UCI ML repository, saves it as a CSV file, and
    validates the data schema.

    Parameters:
    ----------
    write_to : str
        The directory where the CSV file will be written to. Must be an existing directory.

    Returns:
    -------
    None

    """
    check_directory_exists(write_to)
    
    online_shoppers_purchasing_intention_dataset = fetch_ucirepo(id=468) 

    X = online_shoppers_purchasing_intention_dataset.data.features 
    y = online_shoppers_purchasing_intention_dataset.data.targets
    df = pd.concat([X, y], axis=1)
    df.to_csv(os.path.join(write_to, "raw_data.csv"), index= False)


    # validate that the raw data was saved as a csv file
    file_path = os.path.join(write_to, "raw_data.csv")
    assert os.path.isfile(file_path), f"File {file_path} was not created."

    # validate data
    validating_data(df)


if __name__ == '__main__':
    main()
