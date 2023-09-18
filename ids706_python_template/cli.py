"""CLI interface for ids706_python_template project.
"""
import os

from ids706_python_template.lib import (
    describe_data,
    get_female_ds,
    get_male_ds,
    plot_gender_diff,
    plot_overall_salary,
    read_data,
)


def plot(arg, male_ds, female_ds):
    """
    Plot the data
    Args:
        arg: True if prints each gender's salary distribution,
             False if prints the difference between the two
        male_ds: Male dataset
        female_ds: Female dataset

    Returns: None
    """
    if arg:
        plot_overall_salary(male_ds, female_ds)
    else:
        plot_gender_diff(male_ds, female_ds)


def main(plot_function=plot):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(script_dir, "Glassdoor Gender Pay Gap.csv")
    # Check if the file exists and then read it
    if os.path.exists(csv_file_path):
        ds = read_data(csv_file_path)
    else:
        print("CSV file not found:", csv_file_path)
        return

    print("Data description:")
    print(describe_data(ds))

    female_ds = get_female_ds(ds)
    male_ds = get_male_ds(ds)

    print("Plotting overall salary distribution")
    plot_function(True, male_ds, female_ds)

    print("Plotting gender salary difference")
    plot_function(False, male_ds, female_ds)
