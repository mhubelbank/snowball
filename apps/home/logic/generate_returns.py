import numpy as np
import random

def generate_returns(years: int, avg: float = 0.1025, std_dev: float = 0.1) -> list[float]:
    """This is a function designed to generate a list of floats to be used in simulating asset growth in the market

    Parameters
    ----------
    years : int
        The number of years to simulate
    avg : float, optional
        The average return, by default 0.1025
    std_dev : float, optional
        The standard deviation of the return, by default 0.1

    Returns
    -------
    list[float]
        A list of floats representing the rate of return of the US stock market
    """

    np.random.seed(int(random.random() * 100000))
    returns = np.random.normal(loc=avg, scale=std_dev, size=years)
    returns = list(returns)

    return returns