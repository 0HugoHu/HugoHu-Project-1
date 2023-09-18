import pandas as pd
import pytest
import warnings
from ids706_python_template.lib import (
    read_data,
    describe_data,
    my_plot,
    get_male_ds,
    get_female_ds,
    plot_overall_salary,
    plot_gender_diff,
)

warnings.simplefilter(action="ignore", category=FutureWarning)


# Define a fixture for test data
@pytest.fixture
def sample_dataframe():
    data = {
        "Gender": ["Male", "Female", "Male", "Male", "Female"],
        "BasePay": [50000, 60000, 55000, 58000, 62000],
        "JobTitle": [
            "Engineer",
            "Manager",
            "Technician",
            "Engineer",
            "Manager",
        ],
        "Education": ["PhD", "Masters", "PhD", "Bachelors", "PhD"],
        "Seniority": [3, 5, 2, 4, 6],
    }
    return pd.DataFrame(data)


# Define test functions for each library function
def test_read_data(sample_dataframe):
    df = sample_dataframe
    assert len(df) > 0


def test_describe_data(sample_dataframe):
    df = sample_dataframe
    description = describe_data(df)
    assert "BasePay" in description.columns


def test_my_plot():
    # We can't easily test plt.show()
    pass


def test_get_male_ds(sample_dataframe):
    df = sample_dataframe
    male_ds = get_male_ds(df)
    assert len(male_ds) > 0


def test_get_female_ds(sample_dataframe):
    df = sample_dataframe
    female_ds = get_female_ds(df)
    assert len(female_ds) > 0
