import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path):
    data = pd.read_csv(file_path)
    data.columns = data.columns.str.strip()
    print("Columns in the dataset:", data.columns)
    if 'LTP' in data.columns:
        return data['LTP']
    else:
        raise KeyError("The 'LTP' column is not found in the dataset.")

def monte_carlo_simulation(prices, days, trials):
    price_paths = np.zeros((trials, days))
    price_paths[:, 0] = prices.iloc[-1]
    for t in range(1, days):
        random_returns = np.random.normal(0, 0.01, trials)
        price_paths[:, t] = price_paths[:, t - 1] * (1 + random_returns)
    return price_paths

def quantum_analysis(price_paths):
    final_prices = price_paths[:, -1]
    mean_price = np.mean(final_prices)
    std_dev_price = np.std(final_prices)
    return {"mean": mean_price, "std_dev": std_dev_price}

def main():
    file_path = r"C:\National_Stock_Exchange_of_India_Ltd.csv"
    if not os.path.exists(file_path):
        print("The file does not exist. Please check the path.")
        return
    try:
        prices = load_data(file_path)
    except KeyError as e:
        print(f"An error occurred: {e}")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return
    days = int(input("Enter the number of days to simulate: "))
    trials = int(input("Enter the number of trials for the simulation: "))
    price_paths = monte_carlo_simulation(prices, days, trials)
    quantum_results = quantum_analysis(price_paths)
    plt.figure(figsize=(10, 6))
    plt.plot(price_paths.T)
    plt.title('Monte Carlo Simulation of Stock Prices')
    plt.xlabel('Days')
    plt.ylabel('Price')
    plt.show()
    print("Quantum Analysis Results:", quantum_results)

if __name__ == "__main__":
    main()