# eda.py
# Author: Julian Daduica
# Date: 2024-12-03


# This script performs exploratory data analysis (EDA) on the training dataset, generates a description table, and
# visualizations. Then saves them as a CSV and PNG files to the inputted directory.
#
# Usage: python scripts/03_eda.py \
# --data_from=data/processed/train_df.csv \
# --plot_to=results/images/ \
# --tables_to=results/tables/


import click
import os
import altair as alt
import altair_ally as aly
import pandas as pd

@click.command()
@click.option('--data_from', type = str, help = "Path to processed training data")
@click.option('--plot_to', type = str, help = "Path to directory where the plot will be written to")
@click.option('--tables_to', type = str, help = "Path to directory where the tables will be written to")

def main(data_from, tables_to, plot_to):
    """
    Performs exploratory data analysis (EDA) on the training dataset, generates visualizations, and saves them as
    image files.
    
    ----------
    data_from : str
        The file path to the processed training data CSV file.

    plot_to : str
        The directory path where the visualization plots will be saved.

    tables_to : str
        The directory path where the tables will be saved.

    Returns:
    --------
    None
    """


    
    train_df = pd.read_csv(data_from)

    # describe dataset table and save to tables results folder
    describe_table = train_df.describe()
    describe_file_path = os.path.join(tables_to, "train_df_describe.csv")
    describe_table.to_csv(describe_file_path)

        
    # create feature density plot
    aly.alt.data_transformers.enable('vegafusion')

    feature_density_plot = aly.dist(train_df, color='Revenue')

    # save feature density plot
    feature_density_plot.save(os.path.join(plot_to, "feature_density.png"),
              scale_factor=2.0)


    #create feature bar plot
    feature_bar_plot = aly.dist(train_df.assign(churn=lambda df: df['Revenue'].astype(object)), dtype='object', color='Revenue')


    # save feature bar plot
    feature_bar_plot.save(os.path.join(plot_to, "feature_bar_plot.png"),
              scale_factor=2.0)

    
    #make correlation dataframe for correlation heatmap
    corr_df = (
        train_df
        .corr('spearman', numeric_only = True)
        .abs()                      
        .stack()                   
        .reset_index(name = 'corr')
        .query(('level_0 < level_1')))  

    # plot for correlation heatmap
    correlation_heatmap = alt.Chart(corr_df).mark_rect().encode(
        x = alt.X('level_0:N', title = 'Feature 1'),
        y = alt.Y('level_1:N', title = 'Feature 2'),
        size = alt.Size('corr:Q', title = 'Correlation Strength'),
        color = alt.Color('corr:Q'),
        tooltip = ['level_0', 'level_1', 'corr']
    ).properties(
        width = 600,
        height = 600,
        title = "Correlation Heatmap Between all Features"
    )

    # numbers associated with correlation heatmap plot
    correlation_numbers = alt.Chart(corr_df).mark_text(baseline='middle').encode(
        x = alt.X('level_0:N', title='Feature 1'),
        y = alt.Y('level_1:N', title='Feature 2'),
        text=alt.Text('corr:Q', format='.2f')
    )
    
    correlation_heatmap_with_numbers = correlation_heatmap + correlation_numbers


    correlation_heatmap_with_numbers.save(os.path.join(plot_to, "correlation_heatmap.png"),
              scale_factor=2.0)

if __name__ == '__main__':
    main()
    
