import pytest
from ids706_python_template.cli import main
from unittest.mock import Mock
import os


def test_main(mocker):
    # Get the directory containing the cli.py script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Set the current working directory to the directory containing cli.py
    os.chdir(script_dir)

    # Mock the plot function
    mocked_plot = mocker.patch("ids706_python_template.cli.plot")

    # Call the main function with the mocked plot function
    main(plot_function=mocked_plot)

    # Add your assertions here to check the behavior of the main function
    assert mocked_plot.call_count == 2  # Check if plot was called twice
