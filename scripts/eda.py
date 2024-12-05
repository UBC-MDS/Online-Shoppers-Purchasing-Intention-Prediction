# eda.py
# Author: Julian Daduica, Stephanie Ta, WaiMing Wong
# Date: 2024-12-03


import click
import os
import altair as alt
import altair_ally as aly
import pandas as pd

@click.command()
@click.option('--data_from', type = str, help = "Path to processed training data")
@click.option('--plot_to', type = str, help = "Path to directory where the plot will be written to")
def main(data_from, plot_to):
    """
    add description
    """
    train_df = pd.read_csv(data_from)


    #train_df.describe()
    #train_df.info()

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
    
