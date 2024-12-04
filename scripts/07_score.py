# 07_score.py
# author: Stephanie Ta
# date: 2024-12-03
#
# This script scores the dummy and the logistic regression models.
#
# Usage: python scripts/07_score.py \
# --dummy-model-from=results/models/dummy_classifier.pickle \
# --logreg-model-from=results/models/logreg_classifier.pickle \
# --scores-to=results/tables/model_scores.csv \

import pandas as pd
import pickle

@click.option('--dummy-model-from', type=str, help="Path to directory where the dummy model is")
@click.option('--logreg-model-from', type=str, help="Path to directory where the logistic regression model is")
@click.option('--scores-to', type=str, help="Path to directory where the score will be written to")
def main(dummy_model_from, logreg_model_from, scores_to):

    # read in saved dummy model object
    with open(dummy_model_from, 'rb') as f:
        dummy_classifier = pickle.load(f)

    # read in saved logistiv regression model object
    with open(logreg_model_from, 'rb') as f:
        random_search = pickle.load(f)

    # score dummy and best logistic regression model on test set
    dummy_test_score = dummy_classifier.score(X_test, y_test)
    log_reg_test_score = random_search.score(X_test, y_test)

    # save the test accuracy scores
    model_results = pd.read_csv(scores_to)
    model_results['test_accuracy'][0] = dummy_test_score
    model_results['test_accuracy'][1] = log_reg_test_score
    model_results.to_csv(scores_to)

if __name__ == "__main__":
    main()