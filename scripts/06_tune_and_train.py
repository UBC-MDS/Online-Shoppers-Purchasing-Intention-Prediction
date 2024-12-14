# 06_tune_and_train.py
# author: Stephanie Ta
# date: 2024-12-03
#
# This script trains and tunes the logistic regression model
# using RandomSearchCV, then saves the model with the hyperparameters that
# gives the best mean cross validation accuracy.
# It also saves that mean cross validation accuracy score.
#
# Usage: python scripts/06_tune_and_train.py \
# --x-train-data=data/processed/X_train.csv \
# --y-train-data=data/processed/y_train.csv \
# --model-to=results/models/logreg_classifier.pickle \
# --scores-to=results/tables/model_scores.csv

import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import loguniform
import pickle
import click

@click.command()
@click.option('--x-train-data', type=str, help="Path to X training data (features only)")
@click.option('--y-train-data', type=str, help="Path to y training data (target only)")
@click.option('--model-to', type=str, help="Path to directory where the model will be written to")
@click.option('--scores-to', type=str, help="Path to directory where the score will be written to")
def main(x_train_data, y_train_data, model_to, scores_to):
    """
    Trains and tunes the logistic regression model using RandomSearchCV,
    then saves the model with the hyperparameters that gives the best mean cross validation accuracy.
    Also saves that mean cross validation accuracy score.
    """
    # read in data
    X_train = pd.read_csv(x_train_data)
    y_train = pd.read_csv(y_train_data)
    y_train = y_train.to_numpy().ravel()

    # lists of each type of feature
    numeric_cols = ['Administrative_Duration',
                    'Informational_Duration',
                    'ProductRelated_Duration',
                    'BounceRates', 'ExitRates',
                    'PageValues', 'SpecialDay']
    categorical_cols = ['Weekend', 'OperatingSystems',
                        'Browser', 'Region',
                        'TrafficType', 'VisitorType']
    ordinal_cols = ['Month']

    # make preproccessor, note imputation is not needed since there are no null values in the data set
    month_levels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    preprocessor = make_column_transformer(
        (StandardScaler(), numeric_cols),
        (OneHotEncoder(sparse_output=False, handle_unknown='ignore'), categorical_cols),
        (OrdinalEncoder(categories=[month_levels]), ordinal_cols)
    )

    # make pipeline including preprocessor and logistic regression model
    log_reg_pipe = make_pipeline(
        preprocessor, LogisticRegression(max_iter=2000, random_state=123)
    )

    # tune hyperparameter C of the logistic regression model
    param_grid = {
        "logisticregression__C": loguniform(1e-3, 1e3),
    }
    
    random_search = RandomizedSearchCV(
        log_reg_pipe,
        param_grid,
        n_iter=100,
        verbose=1,
        n_jobs=-1,
        random_state=123,
        return_train_score=True,
    )
    
    random_search.fit(X_train, y_train)

    # save logistic regression model object
    with open(model_to, 'wb') as f:
        pickle.dump(random_search, f)
        
    # access best C using: random_search.best_params_['logisticregression__C']

    # save mean logistic regression validation accuracy
    model_results = pd.read_csv(scores_to)
    model_results.loc[1, 'mean_validation_accuracy'] = random_search.best_score_
    model_results.to_csv(scores_to)

if __name__ == "__main__":
    main()
