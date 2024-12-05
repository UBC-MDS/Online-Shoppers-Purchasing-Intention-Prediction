# extract_data.py
# Author: Julian Daduica, Stephanie Ta, WaiMing Wong
# Date: 2024-12-03

from ucimlrepo import fetch_ucirepo # raw data is from this package

import click
import os
import requests
import pandas as pd
import pandera as pa



def check_directory_exists(directory):
    if not os.path.isdir(directory):
        raise ValueError('The directory provided does not exist.')


@click.command()
@click.option('--write_to', type = str, help = "Path to directory where raw data will be written to")
def main(write_to):

    check_directory_exists(write_to)
    
    online_shoppers_purchasing_intention_dataset = fetch_ucirepo(id=468) 

    X = online_shoppers_purchasing_intention_dataset.data.features 
    y = online_shoppers_purchasing_intention_dataset.data.targets
    df = pd.concat([X, y], axis=1)
    df.to_csv(os.path.join(write_to, "raw_data.csv"), index= False)


    # validate that the raw data was saved as a csv file
    #assert os.path.isfile(write_to)

    # validate data
    schema = pa.DataFrameSchema(
        {"Administrative": pa.Column(int, nullable=False),
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

    schema.validate(df, lazy=True)


if __name__ == '__main__':
    main()
