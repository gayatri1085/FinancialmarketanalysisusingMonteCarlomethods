"""
Financial Market Analysis using Monte Carlo Simulation
Author: Gayatri

This script simulates future stock prices using Monte Carlo methods
based on historical price data.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_data(file_path):
    """Load stock price data and return LTP column."""
    data = pd.read_csv(file_path)
    data.columns = data.columns.str.strip()

    if 'LTP' not in data.columns:
        raise ValueError("Dataset must contain 'LTP' column")

    return data['LTP']


def monte_carlo_simulation(prices, days=100, trials=1000):
    """Generate Monte Carlo price paths."""
    mu = prices.pct_change().mean()
    sigma = prices.pct_change().std()

    price_paths = np.zeros((trials, days))
    price_paths[:, 0] = prices.iloc[-1]

    for t in range(1, days):
        random_returns = np.random.normal(mu, sigma, trials)
        price_paths[:, t] = price_paths[:, t - 1] * (1 + random_returns)

    return price_paths


def statistical_analysis(price_paths):
    """Return mean and standard deviation of final prices."""
    final_prices = price_paths[:, -1]
    return {
        "mean_price": np.mean(final_prices),
        "std_dev": np.std(final_prices),
        "min": np.min(final_prices),
        "max": np.max(final_prices),
    }


def plot_simulation(price_paths):
    plt.figure(figsize=(10, 6))
    plt.plot(price_paths.T, alpha=0.1)
    plt.title("Monte Carlo Simulation of Stock Prices")
    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.show()


def main():
    file_path = "data/stock_prices.csv"  # relative path

    prices = load_data(file_path)
    price_paths = monte_carlo_simulation(prices, days=180, trials=2000)
    results = statistical_analysis(price_paths)

    plot_simulation(price_paths)
    print("Statistical Results:", results)


if __name__ == "__main__":
    main()
