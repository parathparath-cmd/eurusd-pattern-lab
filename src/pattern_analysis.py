
import numpy as np
import pandas as pd


def analyze_returns(close: pd.Series) -> pd.DataFrame:
    """Summarize simple next-bar returns and their direction."""
    returns = close.pct_change().dropna()

    if returns.empty:
        raise ValueError("At least two valid closing prices are required.")

    return pd.DataFrame({
        "return": returns,
        "direction": np.where(returns > 0, "up",
                     np.where(returns < 0, "down", "flat")),
    })


def main():
    # Synthetic example only; not real EURUSD market data.
    rng = np.random.default_rng(42)
    changes = rng.normal(0, 0.0005, 1000)
    close = pd.Series(1.10 * np.cumprod(1 + changes))

    results = analyze_returns(close)

    print("EURUSD Pattern Lab — synthetic demonstration")
    print(f"Observations: {len(results)}")
    print(f"Up bars: {(results['direction'] == 'up').sum()}")
    print(f"Down bars: {(results['direction'] == 'down').sum()}")
    print(f"Mean return: {results['return'].mean():.6%}")
    print(f"Return volatility: {results['return'].std():.6%}")


if __name__ == "__main__":
    main()
