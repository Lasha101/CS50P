# Bitcoin Price Analysis

#### Video Demo: [https://youtu.be/CNZqR5cIzwY]

#### Description:
The "Bitcoin Price Analysis" project aims to analyze historical Bitcoin price data and provide insights into the trend, equation, derivative, and inclination slope of the Bitcoin price curve.

This project consists of two files:

- `project.py`: This file contains the main code for Bitcoin price analysis.

- `test_project.py`: This file contains unit tests for the functions and classes in `project.py`.

The code in `project.py` includes the following functions and classes:

- `Data`: A class that encapsulates the years and prices data used for regression analysis. It provides methods to calculate regression coefficients using NumPy's `polyfit` function.

- `get_bitcoin_prices()`: A function that retrieves historical Bitcoin prices from the CoinDesk API and generates random fluctuations for simulation purposes.

- `date()`: A utility function to convert the user-input date to a float value.

- `get_value()`: A function that estimates the Bitcoin price on the given date using the regression equation.

- `make_equation()`: A function that generates a polynomial equation based on the regression coefficients.

- `calculate_derivative()`: A function that calculates the derivative of the polynomial equation and determines the rate of change at the estimated Bitcoin price.

- `inclination_slope()`: A function that calculates the angle of inclination in degrees based on the rate of change.

The `test_project.py` file contains unit tests for the functions in `project.py` to ensure their correctness and functionality.

The tests in `test_project.py` include the following functions:

- `test_date()`: A function that tests the `date()` function to ensure it raises a `ValueError` for invalid inputs.

- `test_calculate_derivative()`: A function that tests the `calculate_derivative()` function with different inputs to verify its correctness.

- `test_inclination_slope()`: A function that tests the `inclination_slope()` function with different inputs to verify its correctness.

To use this project, execute the `project.py` file. It will perform Bitcoin price analysis based on the provided code. You can also run the unit tests in `test_project.py` to verify the correctness of the implemented functions and classes.

Please note that the historical Bitcoin price data in this project is simulated. For actual price analysis, consider replacing the random fluctuations with real historical price data.

Feel free to explore the code, make modifications, and adapt it to suit your specific needs and requirements. Happy analyzing!
