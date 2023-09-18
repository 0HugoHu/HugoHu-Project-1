"""
ids706_python_template lib module.
"""
import warnings

import matplotlib.pyplot as plt
import pandas as pd
import plotly.figure_factory as ff
import seaborn as sns

warnings.simplefilter(action="ignore", category=FutureWarning)


def read_data(path):
    """
    Read data from csv file
    Args:
        path: path to csv file

    Returns: pandas dataframe
    """
    df = pd.read_csv(path)
    return df


def describe_data(df):
    """
    Describe data
    Args:
        df: pandas dataframe

    Returns: pandas dataframe
    """
    return df.describe()


def my_plot(x, color):
    """
    Plot distribution of a variable
    Args:
        x: variable to plot
        color: color of the plot

    Returns: None
    """
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 6)
    sns.histplot(x, bins=100, color=color)
    plt.show()


def get_male_ds(df):
    """
    Get male dataset
    Args:
        df: pandas dataframe

    Returns: pandas dataframe
    """
    return df[df["Gender"] == "Male"].loc[
        :, ["BasePay", "JobTitle", "Education", "Seniority"]
    ]


def get_female_ds(df):
    """
    Get female dataset
    Args:
        df: pandas dataframe

    Returns: pandas dataframe
    """
    return df[df["Gender"] == "Female"].loc[
        :, ["BasePay", "JobTitle", "Education", "Seniority"]
    ]


def plot_overall_salary(male_ds, female_ds):
    """
    Plot overall salary distribution
    Args:
        male_ds: Male dataset
        female_ds: Female dataset

    Returns: None
    """
    my_plot(male_ds["BasePay"], "blue")
    my_plot(female_ds["BasePay"], "red")


def plot_gender_diff(male_ds, female_ds):
    """
    Plot gender difference
    Args:
        male_ds: Male dataset
        female_ds: Female dataset

    Returns: None
    """
    data = [male_ds["BasePay"], female_ds["BasePay"]]

    group_labels = ["Male", "Female"]
    colors = ["#00a000", "#e74c3c"]

    # Create dist plot with curve_type set to 'normal'
    fig = ff.create_distplot(
        data, group_labels, show_hist=False, colors=colors
    )

    # Add title
    fig.update_layout(title_text="Symmetry")
    fig.show()
