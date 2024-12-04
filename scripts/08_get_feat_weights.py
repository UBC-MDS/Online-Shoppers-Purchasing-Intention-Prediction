# 08_get_feat_weights.py
# author: Stephanie Ta
# date: 2024-12-04
#
# This script gets the feature weights (as magnitude) from the logistic regression model
# saves them in a table. It also visualizes the weights in a bar chart and
# saves the bar chart.
#
# Usage: python 08_get_feat_weights.py \
# --logreg-model-from=results/models/logreg_classifier.pickle \
# --scores-to=results/tables/model_scores.csv \
# --figure-to=results/figures/fig4_feat_weights.png

import pandas as pd
import pickle
import altair as alt

@click.option('--logreg-model-from', type=str, help="Path to directory where the logistic regression model is")
@click.option('--weights-to', type=str, help="Path to directory where the feature weights will be written to")
@click.option('--figure-to', type=str, help="Path to directory where the figure of feature weights will be written to")
def main(logreg_model_from, scores_to, scores_to, figure_to):
    
    # read in saved logistic regression model object
    with open(logreg_model_from, 'rb') as f:
        random_search = pickle.load(f)

    # find weights of each feature
    best_estimator = random_search.best_estimator_
    feature_names = best_estimator['columntransformer'].get_feature_names_out() # get feature names
    weights = best_estimator["logisticregression"].coef_ # get feature coefficients

    feat_weights = pd.DataFrame(weights, columns = feature_names)
    feat_weights = feat_weights.T.reset_index()
    feat_weights = feat_weights.rename(columns={'index': 'feature', 0: "weight"})
    feat_weights['feature'] = feat_weights['feature'].str.split('__', expand = True)[1]

    # average the weights of each overall feature and 
    # absolute value the weights so that positive and negative ones don't cancel eachother out
    feat_weights['overall_feature'] = feat_weights['feature'].str.split('_', expand = True)[0]
    feat_weights['absolute_value_weight'] = abs(feat_weights['weight'])
    absolute_feat_weights = pd.DataFrame(feat_weights.groupby('overall_feature'
        ).mean(numeric_only=True
        ).sort_values('absolute_value_weight', ascending = False
        )['absolute_value_weight']).reset_index()

    # save weights in csv
    absolute_feat_weights.to_csv(scores_to)

    # visualize the magnitude of the weights in a bar graph
    magnitude_bar_graph = alt.Chart(absolute_feat_weights).mark_bar().encode(
        x = alt.X('absolute_value_weight').title('Absolute Value Weight'),
        y = alt.Y('overall_feature').sort('x').title('Overall Feature')

    # save figure as png
    magnitude_bar_graph.save(figure_to)

if __name__ == "__main__":
    main()