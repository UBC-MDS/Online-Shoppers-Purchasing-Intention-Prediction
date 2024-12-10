# Makefile
# Stephanie Ta
# date: 2024-12-10

# This driver script completes the analysis of our project
# This script takes no arguments.

# example usage:
# make all

.PHONY : all \
data \
tables \
images \
models \
clean-data \
clean-tables \
clean-images \
clean-models \
clean-report \
clean

all : data \
tables \
images \
models \
reports/online_shoppers_purchasing_intention_prediction.pdf reports/online_shoppers_purchasing_intention_prediction.html

# data
data : raw_data.csv \
data/processed/train_df.csv \
data/processed/test_df.csv \
data/processed/X_train.csv \
data/processed/y_train.csv \
data/processed/X_test.csv \
data/processed/y_test.csv

raw_data.csv : scripts/01_extract_data.py
    python scripts/01_extract_data.py --write_to=data/raw/

data/processed/train_df.csv : scripts/02_split_data.py scripts/04_preprocess_and_validate.py data/raw/raw_data.csv
    python scripts/02_split_data.py --raw_data=data/raw/raw_data.csv --data_to=data/processed/
    python scripts/04_preprocess_and_validate.py \
        --train-data=data/processed/train_df.csv \
        --test-data=data/processed/test_df.csv \
        --x-train-data=data/processed/X_train.csv \
        --x-test-data=data/processed/X_test.csv

data/processed/test_df.csv : scripts/02_split_data.py scripts/04_preprocess_and_validate.py data/raw/raw_data.csv
    python scripts/02_split_data.py --raw_data=data/raw/raw_data.csv --data_to=data/processed/
    python scripts/04_preprocess_and_validate.py \
        --train-data=data/processed/train_df.csv \
        --test-data=data/processed/test_df.csv \
        --x-train-data=data/processed/X_train.csv \
        --x-test-data=data/processed/X_test.csv

data/processed/X_train.csv : scripts/02_split_data.py scripts/04_preprocess_and_validate.py data/raw/raw_data.csv
    python scripts/02_split_data.py --raw_data=data/raw/raw_data.csv --data_to=data/processed/
    python scripts/04_preprocess_and_validate.py \
        --train-data=data/processed/train_df.csv \
        --test-data=data/processed/test_df.csv \
        --x-train-data=data/processed/X_train.csv \
        --x-test-data=data/processed/X_test.csv

data/processed/y_train.csv : scripts/02_split_data.py data/raw/raw_data.csv
    python scripts/02_split_data.py --raw_data=data/raw/raw_data.csv --data_to=data/processed/

data/processed/X_test.csv : scripts/02_split_data.py scripts/04_preprocess_and_validate.py data/raw/raw_data.csv
    python scripts/02_split_data.py --raw_data=data/raw/raw_data.csv --data_to=data/processed/
    python scripts/04_preprocess_and_validate.py \
        --train-data=data/processed/train_df.csv \
        --test-data=data/processed/test_df.csv \
        --x-train-data=data/processed/X_train.csv \
        --x-test-data=data/processed/X_test.csv

data/processed/y_test.csv : scripts/02_split_data.py data/raw/raw_data.csv
    python scripts/02_split_data.py --raw_data=data/raw/raw_data.csv --data_to=data/processed/

# tables
tables : results/tables/train_df_describe.csv \
results/tables/model_scores.csv \
results/tables/feat_weights.csv

results/tables/train_df_describe.csv : scripts/03_eda.py data/processed/train_df.csv
    python scripts/03_eda.py \
        --data_from=data/processed/train_df.csv \
        --plot_to=results/images/ \
        --tables_to=results/tables/

results/tables/model_scores.csv : scripts/05_dummy.py data/processed/X_train.csv data/processed/y_train.csv scripts/06_tune_and_train.py scripts/07_score.py results/models/dummy_classifier.pickle results/models/logreg_classifier.pickle
    python scripts/05_dummy.py \
        --x-train-data=data/processed/X_train.csv \
        --y-train-data=data/processed/y_train.csv \
        --model-to=results/models/dummy_classifier.pickle \
        --scores-to=results/tables/model_scores.csv
    python scripts/06_tune_and_train.py \
        --x-train-data=data/processed/X_train.csv \
        --y-train-data=data/processed/y_train.csv \
        --model-to=results/models/logreg_classifier.pickle \
        --scores-to=results/tables/model_scores.csv
    python scripts/07_score.py \
        --dummy-model-from=results/models/dummy_classifier.pickle \
        --logreg-model-from=results/models/logreg_classifier.pickle \
        --scores-to=results/tables/model_scores.csv \
        --x-test-data=data/processed/X_test.csv \
        --y-test-data=data/processed/y_test.csv

results/tables/feat_weights.csv : scripts/08_get_feat_weights.py results/models/logreg_classifier.pickle
    python scripts/08_get_feat_weights.py \
        --logreg-model-from=results/models/logreg_classifier.pickle \
        --weights-to=results/tables/feat_weights.csv \
        --figure-to=results/images/fig4_feat_weights.png


# images
images : results/images/feature_density.png \
results/images/feature_bar_plot.png \
results/images/correlation_heatmap.png \
results/images/fig4_feat_weights.png

results/images/feature_density.png : scripts/03_eda.py data/processed/train_df.csv
    python scripts/03_eda.py \
        --data_from=data/processed/train_df.csv \
        --plot_to=results/images/ \
        --tables_to=results/tables/

results/images/feature_bar_plot.png : scripts/03_eda.py data/processed/train_df.csv
    python scripts/03_eda.py \
        --data_from=data/processed/train_df.csv \
        --plot_to=results/images/ \
        --tables_to=results/tables/

results/images/correlation_heatmap.png : scripts/03_eda.py data/processed/train_df.csv
    python scripts/03_eda.py \
        --data_from=data/processed/train_df.csv \
        --plot_to=results/images/ \
        --tables_to=results/tables/

results/images/fig4_feat_weights.png : scripts/08_get_feat_weights.py results/models/logreg_classifier.pickle
    python scripts/08_get_feat_weights.py \
        --logreg-model-from=results/models/logreg_classifier.pickle \
        --weights-to=results/tables/feat_weights.csv \
        --figure-to=results/images/fig4_feat_weights.png

# models
models : results/models/dummy_classifier.pickle \
results/models/logreg_classifier.pickle

results/models/dummy_classifier.pickle : scripts/05_dummy.py data/processed/X_train.csv data/processed/y_train.csv
    python scripts/05_dummy.py \
        --x-train-data=data/processed/X_train.csv \
        --y-train-data=data/processed/y_train.csv \
        --model-to=results/models/dummy_classifier.pickle \
        --scores-to=results/tables/model_scores.csv

results/models/logreg_classifier.pickle : scripts/06_tune_and_train.py data/processed/X_train.csv data/processed/y_train.csv
    python scripts/06_tune_and_train.py \
        --x-train-data=data/processed/X_train.csv \
        --y-train-data=data/processed/y_train.csv \
        --model-to=results/models/logreg_classifier.pickle \
        --scores-to=results/tables/model_scores.csv

# render report
reports/online_shoppers_purchasing_intention_prediction.pdf reports/online_shoppers_purchasing_intention_prediction.html : reports/online_shoppers_purchasing_intention_prediction.qmd
    quarto render reports/online_shoppers_purchasing_intention_prediction.qmd

# clean outputs
clean-data :
    rm -f raw_data.csv \
        data/processed/train_df.csv \
        data/processed/test_df.csv \
        data/processed/X_train.csv \
        data/processed/y_train.csv \
        data/processed/X_test.csv \
        data/processed/y_test.csv

clean-tables :
    rm -f results/tables/train_df_describe.csv \
        results/tables/model_scores.csv \
        results/tables/feat_weights.csv

clean-images :
 rm -f results/images/feature_density.png \
        results/images/feature_bar_plot.png \
        results/images/correlation_heatmap.png \
        results/images/fig4_feat_weights.png

clean-models :
    rm -f results/models/dummy_classifier.pickle \
        results/models/logreg_classifier.pickle

clean-report :
    rm -f reports/online_shoppers_purchasing_intention_prediction.pdf \
        reports/online_shoppers_purchasing_intention_prediction.html \
    rm -rf reports/online_shoppers_purchasing_intention_prediction_files

clean : clean-data clean-tables clean-images clean-models clean-report