# 04_preprocess_and_validate.py
# author: Stephanie Ta
# date: 2024-12-03
#
# This script creates the baseline model to compare our final model to.
#
# Usage: python scripts/05_dummy.py \
# --X-train-data=data/processed/X_train.csv \
# --y-train-data=data/processed/y_train.csv \


# create baseline model to compare final model to
dummy_classifier = DummyClassifier()
dummy_classifier.fit(X_train, y_train)
dummy_cv_scores = pd.DataFrame(
    cross_validate(dummy_classifier, X_train, y_train, cv = 5, return_train_score = True))
mean_dummy_validation_accuracy = dummy_cv_scores['test_score'].mean()
mean_dummy_validation_accuracy