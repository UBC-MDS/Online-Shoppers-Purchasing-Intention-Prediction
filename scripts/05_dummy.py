# 05_dummy.py
# author: Stephanie Ta
# date: 2024-12-03
#
# This script creates and saves the baseline model to compare our final model to.
# It also saves the validation accuracy of the baseline model
#
# Usage: python scripts/05_dummy.py \
# --X-train-data=data/processed/X_train.csv \
# --y-train-data=data/processed/y_train.csv \
# --model-to=results/models/dummy_classifier.pickle \
# --scores-to=results/tables/model_scores.csv \

import pandas as pd
from sklearn.model_selection import cross_validate
from sklearn.dummy import DummyClassifier
import pickle

@click.option('--X-train-data', type=str, help="Path to X training data (features only)")
@click.option('--y-train-data', type=str, help="Path to y training data (target only)")
@click.option('--model-to', type=str, help="Path to directory where the model will be written to")
@click.option('--scores-to', type=str, help="Path to directory where the score will be written to")
def main(X_train_data, y_train_data, model_to, scores_to):
    # read in data
    X_train = pd.read_csv(X_train_data)
    y_train = pd.read_csv(y_train_data)
    
    # create baseline model to compare final model to
    dummy_classifier = DummyClassifier()
    dummy_classifier.fit(X_train, y_train)

    # save baseline model object
    with open(model_to, 'wb') as f:
        pickle.dump(dummy_classifier, f)
    
    dummy_cv_scores = pd.DataFrame(
        cross_validate(dummy_classifier, X_train, y_train, cv = 5, return_train_score = True))

    # save mean dummy validation accuracy
    model_results = pd.DataFrame({
        'model': ['Dummy Model', 'Logistic Regression Model'],
        'mean_validation_accuracy': [dummy_cv_scores['test_score'].mean(), None],
        'test_accuracy': [None, None]
    })
    model_results.to_csv(scores_to)

if __name__ == "__main__":
    main()