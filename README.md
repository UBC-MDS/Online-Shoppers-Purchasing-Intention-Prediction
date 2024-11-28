# Online Shoppers Purchasing Intention Prediction
Authors: Julian Daduica @jdaduica, Stephanie Ta @Stephanie-Ta, and Wai Ming Wong @waiming


# About
This study attempts to build a classification model using a logistic regression algorithm to predict whether an online shopper will make a purchase based on their website interaction behaviour. The final classifier model achieved an accuracy of 87.5% on an unseen test dataset. Compare this to a dummy classifier model that always predicts no purchase, with an accuracy of 83.5%. While the logistic regression model performed reasonably well, it did not account for the class imbalance in the dataset, where there purchase target class was significantly less than the no purchase target class. From our logistic regression model, we identified that features PageValue and ExitRate were most important when making predictions. This can suggest that these features are the most significant when determining whether a customer will purchase or not. This model can provide insight for businesses to increase revenue by targeting and optimizing these features in marketing or sales campaigns. Further research addressing class imbalance and exploring alternative models or algorithms could improve predictions, which will increase the model’s ability for businesses to utilize. 

# Report
The final report can be found [here](https://github.com/UBC-MDS/Online-Shoppers-Purchasing-Intention-Prediction/blob/main/src/online_shoppers_purchasing_intention_prediction.ipynb)

# Usage
We are using a Docker virtual container so that our computational environment is reproducible. Please ensure that Docker Desktop is running while replicating our analysis if you are using Windows or Mac.

To replicate our analysis:
1. Clone this GitHub repository to your local machine and navigate to the project root.
2. Launch the virtual container by running the command `docker compose up` in terminal.
3. To open JupyterLab, copy and paste the URL in your browser that appears in terminal that starts with `http://127.0.0.1:8888/lab?token=`.
4. In JupyterLab, open our report `src/online_shoppers_purchasing_intention_prediction.ipynb`.
5. Run the report from top to bottom in the JupyterLab web application:
    - Under the `Kernel` tab, click on `Restart Kernel and Run All Cells...`

To exit and clean up the container:
1. `Ctrl` + `C` in terminal where you launched the container.
2. Run the command `docker compose rm` in terminal.

# Dependencies
- [Docker](https://www.docker.com/)

# How to Update the Container
If you would like to add another package to the container,
please have the following dependencies and follow the instructions below.

## Developer Dependencies
- `conda` (version 24.7.1 or higher)
- `conda-lock` (version 2.5.7 or higher)
- `mamba` (version 1.5.8 or higher)

## How to Add a Package to the Container
1. Create a new branch and add the new package with its version pinned in `environment.yaml`.
2. Update the `conda-linux-64.lock` file by running the command `conda-lock -k explicit --file environment.yaml -p linux-64` in terminal.
3. Ensure the Docker image runs properly by re-building the image locally.
4. If the image runs properly, push the your changes to GitHub and the new image will be published on DockerHub automatically.
5. Update `docker-compose.yml` to use the new image by changing the tag (`image: stephanieta/dsci522-online-shopping-project:<tag>`).
6. Make a pull request to merge your changes to the `main` branch.

# License
The code of this project licensed under the terms of the MIT license. If re-using/re-mixing please provide attribution and link to this webpage.  
The project report is under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) license.
