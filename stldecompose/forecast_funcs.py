# example one-step-ahead forecasting functions 
# implementations based on https://www.otexts.org/fpp

import numpy as np


def naive(data, **kwargs):
    """The naive forecast for the next point is the value of the previous point. 

    In most forecasting situations, the naive model is a good baseline due to it's simplicity 
    and low computational overhead. 

    Args:
        data (np.array): Observed data, presumed to be ordered in time.

    Returns:
        float: a single-valued forecast for the next value in the series.
    """
    forecast = data[-1]
    return forecast


def seasonal_naive(data, n=7, **kwargs):
    """The seasonal naive forecast for the next point is the value observed ``n`` points
    prior in the series. 

    The seasonal parameter (``n``) does not have units of time, but rather units of one 
    observation. For example, to account for weekly cycles within daily observations, ``n=7``.

    Args:
        data (np.array): Observed data, presumed to be ordered in time.
        n (int): period of data seasonality 

    Returns:
        float: a single-valued forecast for the next value in the series.
    """
    forecast = data[-n]
    return forecast


def mean(data, n=3, **kwargs):
    """The mean forecast for the next point is the mean value of the previous ``n`` points in 
    the series.

    Args:
        data (np.array): Observed data, presumed to be ordered in time.
        n (int): period over which to calculate the mean 

    Returns:
        float: a single-valued forecast for the next value in the series.
    """
    # don't start averaging until we've seen n points
    if len(data[-n:]) < n:
        forecast = np.nan
    else:
        # nb: we'll keep the forecast as a float
        forecast = np.mean(data[-n:])
    return forecast


def drift(data, n=3, **kwargs):
    """The drift forecast for the next point is a linear extrapolation from the previous ``n`` 
    points in the series.

    Args:
        data (np.array): Observed data, presumed to be ordered in time.
        n (int): period over which to calculate linear model for extrapolation 

    Returns: 
        float: a single-valued forecast for the next value in the series.
    """
    yi = data[-n]
    yf = data[-1]
    slope = (yf - yi) / (n - 1)
    forecast = yf + slope
    return forecast
