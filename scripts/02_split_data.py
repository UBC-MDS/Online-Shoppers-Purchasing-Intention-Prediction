# split_data.py
# Author: Julian Daduica, Stephanie Ta, WaiMing Wong
# Date: 2024-12-03


import click
import os
import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split



@click.command()
@click.option('--raw_data', type = str, help = "Path to raw data")
@click.option('--data_to', type = str, help = "Path to directory where processed data will be written to")
def main(raw_data, data_to):
    # split the training set and testing set and save them as csv files
    df = pd.read_csv(raw_data)
    train_df, test_df = train_test_split(df, test_size=0.3, random_state=123)
    
    train_df.to_csv(os.path.join(data_to, "train_df.csv"), index= False)
    test_df.to_csv(os.path.join(data_to, "test_df.csv"), index= False)


    X_train = train_df.drop(columns=["Revenue"])
    X_test = test_df.drop(columns=["Revenue"])
    y_train = train_df["Revenue"]
    y_test = test_df["Revenue"]

    X_train.to_csv(os.path.join(data_to, "X_train.csv"), index= False)
    y_train.to_csv(os.path.join(data_to, "y_train.csv"), index= False)
    X_test.to_csv(os.path.join(data_to, "X_test.csv"), index= False)
    y_test.to_csv(os.path.join(data_to, "y_test.csv"), index= False)
    

    # validate that the training and testing sets were saved as csv files
    #assert os.path.isfile(data_to)
    #assert os.path.isfile(data_to)


if __name__ == '__main__':
    main()
