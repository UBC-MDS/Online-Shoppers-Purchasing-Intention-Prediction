# 04_preprocess_and_validate.py
# author: Stephanie Ta
# date: 2024-12-03
#
# This script preprocesses the training and testing data by dropping
# features with high feature-feature correlations. It also validates the
# training data for anomalous correlations between target variable and features
# and anomalous correlations between features
#
# Usage: python scripts/04_preprocess_and_validate.py \
# --train-data=data/processed/train_df.csv \
# --test-data=data/processed/test_df.csv \
# --X-train-data=data/processed/X_train.csv \
# --X-test-data=data/processed/X_test.csv \

import pandas as pd
from deepchecks.tabular.checks import FeatureLabelCorrelation, FeatureFeatureCorrelation
from deepchecks.tabular import Dataset

@click.command()
@click.option('--train-data', type=str, help="Path to training data")
@click.option('--test-data', type=str, help="Path to testing data")
@click.option('--X-train-data', type=str, help="Path to X training data (features only)")
@click.option('--X-test-data', type=str, help="Path to X testing data (features only)")
def main(train_data, test_data, X_train_data, X_test_data):
    # read in data
    train_df = pd.read_csv(train_data)
    test_df = pd.read_csv(test_data)
    X_train = pd.read_csv(X_train_data)
    X_test = pd.read_csv(X_test_data)
    
    # drop features with high feature - feature correlations
    train_df = train_df.drop(columns = ["Administrative", 
                                        "Informational", 
                                        "ProductRelated"])
    
    test_df = test_df.drop(columns = ["Administrative", 
                                      "Informational", 
                                      "ProductRelated"])

    X_train = X_train.drop(columns = ["Administrative", 
                                      "Informational", 
                                      "ProductRelated"])
    
    X_test = X_test.drop(columns = ["Administrative", 
                                      "Informational", 
                                      "ProductRelated"])
    
    # update saved data 
    train_df.to_csv(train_data)
    test_df.to_csv(test_data)
    X_train.to_csv(X_train_data)
    X_test.to_csv(X_test_data)
    
    train_df_data_valid = Dataset(train_df, label="Revenue", cat_features=[])
    
    # the maximum threshold allowed
    threshold = 0.80
    
    # validate training data for anomalous correlations between target variable and features
    check_feature_target_corr = FeatureLabelCorrelation().add_condition_feature_pps_less_than(threshold)
    check_feature_terget_corr_result = check_feature_target_corr.run(dataset = train_df_data_valid)
    
    if not check_feature_terget_corr_result.passed_conditions():
        raise ValueError(f"Feature-target correlation exceeds the maximum acceptable threshold of {threshold}.")
    
    # validate training data anomalous correlations between features
    check_feature_feature_corr = FeatureFeatureCorrelation().add_condition_max_number_of_pairs_above_threshold(threshold = threshold)
    check_feature_feature_corr_result = check_feature_feature_corr.run(dataset = train_df_data_valid)
    
    if not check_feature_feature_corr_result.passed_conditions():
        raise ValueError(f"Feature-feature correlation exceeds the maximum acceptable threshold of {threshold}.")

if __name__ == "__main__":
    main()