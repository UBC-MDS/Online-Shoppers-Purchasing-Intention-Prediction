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
    

if __name__ == "__main__":
    main()