# Financial Market Analysis using Monte Carlo Methods

## Overview
This project applies **Monte Carlo simulation techniques** to analyze and forecast future stock price movements based on historical market data.  
The goal is to model uncertainty in financial markets and estimate possible price distributions under different random scenarios.

---

## Problem Statement
Financial markets are highly volatile and uncertain. Traditional deterministic models often fail to capture this randomness.

This project aims to:
- Simulate multiple future price paths.
- Estimate expected returns and risk.
- Visualize the probability distribution of stock prices.

---

## Methodology

### 1. Data Collection
Historical stock price data is used as the base input for the simulation.

### 2. Monte Carlo Simulation
Thousands of random price paths are generated using:
- Historical mean returns.
- Volatility (standard deviation).
- Random Gaussian noise.

Mathematical model:
S(t) = S(0) * exp((μ - 0.5σ²)t + σ√t * Z)


Where:
- μ = mean return  
- σ = volatility  
- Z = random variable ~ N(0,1)

---

## Results
The simulation produces:
- A distribution of possible future stock prices.
- Visual plots showing price evolution.
- Risk insights such as potential downside and upside.

---

## Key Learnings
- Monte Carlo methods are powerful for modeling uncertainty.
- Higher volatility leads to wider price distributions.
- Probabilistic models provide better risk insight than single-point predictions.

---

## Tech Stack
- Python  
- NumPy  
- Pandas  
- Matplotlib  

---

## How to Run
```bash
pip install -r requirements.txt
python montecarlomethod.py

Output: 
![Screenshot 2024-11-12 124240](https://github.com/user-attachments/assets/f67dc2b8-b87b-42a2-99c0-679d9fbcb1d9)
![Screenshot 2024-11-12 124256](https://github.com/user-attachments/assets/677b9187-88d1-4597-a769-81330163b9fe)



