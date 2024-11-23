# Online Shoppers Purchasing Intention Prediction
Authors: Julian Daduica @jdaduica, Stephanie Ta @Stephanie-Ta, and Wai Ming Wong @waiming


# About
This study attempts to build a classification model using a logistic regression algorithm to predict whether an online shopper will make a purchase based on their website interaction behaviour. The final classifier model achieved an accuracy of 87.5% on an unseen test dataset. Compare this to a dummy classifier model that always predicts no purchase, with an accuracy of 83.5%. While the logistic regression model performed reasonably well, it did not account for the class imbalance in the dataset, where there purchase target class was significantly less than the no purchase target class. From our logistic regression model, we identified that features PageValue and ExitRate were most important when making predictions. This can suggest that these features are the most significant when determining whether a customer will purchase or not. This model can provide insight for businesses to increase revenue by targeting and optimizing these features in marketing or sales campaigns. Further research addressing class imbalance and exploring alternative models or algorithms could improve predictions, which will increase the model’s ability for businesses to utilize. 

# Report
The final report can be found [here](https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/blob/main/src/online-shoppers-purchasing-intention-prediction.html)

# Usage
We are using a conda virtual environment so that our computational environment is reproducible.

To replicate our analysis:
1. Clone this GitHub repository to your local machine and navigate to the project root.
2. Create an environment from the `conda-lock.yml` file by running the command `conda-lock install --name online-shopping-prediction conda-lock.yml` in terminal.
3. Activate the environment by running the command `conda activate online-shopping-prediction`.
4. Open JupyterLab by running the command `jupyter lab` in terminal.
5. Change the kernel in the JupyerLab web application:
    - Under the `Kernel` tab, click on `Change Kernel...`
    - Select the `Python [conda env:online-shopping-prediction]` option in the dropdown that pops up.
6. Run the report from top to bottom in the JupyterLab web application:
    - Under the `Kernel` tab, click on `Restart Kernel and Run All Cells...`

# Dependencies
- `conda` (version 24.7.1 or higher)
- `mamba`(version 1.5.8 or higher)
- `conda-lock` (version 2.5.7 or higher)
- `nb_conda_kernels` (version 2.3.1 or higher)
- `jupyter lab` (version 4.2.0 or higher)
- Python and packages listed in [environment.yaml](https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/blob/main/environment.yaml)

# License
The code of this project licensed under the terms of the MIT license. If re-using/re-mixing please provide attribution and link to this webpage.  
The project report is under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) license.
