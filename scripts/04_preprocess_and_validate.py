# 04_preprocess_and_validate.py
# author: Stephanie Ta
# date: 2024-12-03
#
# This script preprocesses the training and testing data by dropping
# features with high feature-feature correlations. It also validates the
# training data for anomalous correlations between target variable and features
# and anomalous correlations between features
#
# Usage: python 04_preprocess_and_validate.py

import pandas as pd
from deepchecks.tabular.checks import FeatureLabelCorrelation, FeatureFeatureCorrelation
from deepchecks.tabular import Dataset

@click.command()
@click.option()

def main():
    # drop features with high feature - feature correlations
    train_df = train_df.drop(columns = ["Administrative", 
                                        "Informational", 
                                        "ProductRelated"])
    
    test_df = test_df.drop(columns = ["Administrative", 
                                      "Informational", 
                                      "ProductRelated"])
    
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