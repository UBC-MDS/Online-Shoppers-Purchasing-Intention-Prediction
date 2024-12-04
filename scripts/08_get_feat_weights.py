# 08_get_feat_weights.py
# author: Stephanie Ta
# date: 2024-12-03
#
# This script gets the feature weights (as magnitude) from the logistic regression model
# saves them in a table. It also visualizes the weights in a bar chart and
# saves the bar chart.
#
# Usage: python 08_get_feat_weights.py \
# --dummy-model-from=results/models/dummy_classifier.pickle \
# --logreg-model-from=results/models/logreg_classifier.pickle \
# --scores-to=results/tables/model_scores.csv \

import pandas as pd
import pickle
import altair as alt

@click.option('--logreg-model-from', type=str, help="Path to directory where the logistic regression model is")
@click.option('--weights-to', type=str, help="Path to directory where the feature weights will be written to")
@click.option('--figure-to', type=str, help="Path to directory where the figure of feature weights will be written to")
def main(logreg_model_from, scores_to, scores_to, figure_to):
    
    # read in model

    # save weights in csv

    # save figure as png


if __name__ == "__main__":
    main()