---
editor_options: 
  markdown: 
    wrap: sentence
---

# Online Shoppers Purchasing Intention Prediction

Authors: Julian Daduica @jdaduica, Stephanie Ta @Stephanie-Ta, and Wai Ming Wong @waiming

# About

This study attempts to build a classification model using a logistic regression algorithm to predict whether an online shopper will make a purchase based on their website interaction behaviour.
The final classifier model achieved an accuracy of 87.6% on an unseen test dataset.
Compare this to a dummy classifier model that always predicts no purchase, with an accuracy of 83.5%.
While the logistic regression model performed reasonably well, it did not account for the class imbalance in the dataset, where there purchase target class was significantly less than the no purchase target class.
From our logistic regression model, we identified that features PageValue and ExitRate were most important when making predictions.
This can suggest that these features are the most significant when determining whether a customer will purchase or not.
This model can provide insight for businesses to increase revenue by targeting and optimizing these features in marketing or sales campaigns.
Further research addressing class imbalance and exploring alternative models or algorithms could improve predictions, which will increase the model’s ability for businesses to utilize.

# Report

The final report can be found [here](https://ubc-mds.github.io/Online-Shoppers-Purchasing-Intention-Prediction/reports/online_shoppers_purchasing_intention_prediction.html)

# Usage

We are using a Docker virtual container so that our computational environment is reproducible.
Please ensure that Docker Desktop is running while replicating our analysis if you are using Windows or Mac.

To replicate our analysis: 1.
Clone this GitHub repository to your local machine and navigate to the project root.
2.
Launch the virtual container by running the command `docker compose up` in terminal.
3.
To open JupyterLab, copy and paste the URL in your browser that appears in terminal that starts with `http://127.0.0.1:8888/lab?token=`.
4.
Run the following commands in terminal:

```         
python scripts/01_extract_data.py --write_to=data/raw/

python scripts/02_split_data.py --raw_data=data/raw/raw_data.csv --data_to=data/processed/

python scripts/03_eda.py \
     --data_from=data/processed/train_df.csv \
     --plot_to=results/images/ \
     --tables_to=results/tables/

python scripts/04_preprocess_and_validate.py \
    --train-data=data/processed/train_df.csv \
    --test-data=data/processed/test_df.csv \
    --x-train-data=data/processed/X_train.csv \
    --x-test-data=data/processed/X_test.csv

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

python scripts/08_get_feat_weights.py \
    --logreg-model-from=results/models/logreg_classifier.pickle \
    --weights-to=results/tables/feat_weights.csv \
    --figure-to=results/images/fig4_feat_weights.png

quarto render reports/online_shoppers_purchasing_intention_prediction.qmd
```

To exit and clean up the container: 1.
`Ctrl` + `C` in terminal where you launched the container.
2.
Run the command `docker compose rm` in terminal.

# Dependencies

-   [Docker](https://www.docker.com/)

# How to Update the Container

If you would like to add another package to the container, please have the following dependencies and follow the instructions below.

## Developer Dependencies

-   `conda` (version 24.7.1 or higher)
-   `conda-lock` (version 2.5.7 or higher)
-   `mamba` (version 1.5.8 or higher)

## How to Add a Package to the Container

1.  Create a new branch and add the new package with its version pinned in `environment.yaml`.
2.  Update the `conda-linux-64.lock` file by running the command `conda-lock -k explicit --file environment.yaml -p linux-64` in terminal.
3.  Ensure the Docker image runs properly by re-building the image locally.
4.  If the image runs properly, push the your changes to GitHub and the new image will be published on DockerHub automatically.
5.  Update `docker-compose.yml` to use the new image by changing the tag (`image: stephanieta/dsci522-online-shopping-project:<tag>`).
6.  Make a pull request to merge your changes to the `main` branch.

# License

The code of this project licensed under the terms of the MIT license.
If re-using/re-mixing please provide attribution and link to this webpage.\
The project report is under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) license.
