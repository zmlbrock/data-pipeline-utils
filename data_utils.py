#!/usr/bin/env python3
"""
Data pipeline utilities
"""

import requests
import pandas as pd
import numpy as np


def fetch_data(url: str) -> dict:
    """Fetch data from a URL using requests library."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return {}


def process_data(data: dict) -> pd.DataFrame:
    """Process JSON data into a pandas DataFrame."""
    if not data:
        return pd.DataFrame()
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    return df


if __name__ == "__main__":
    # Example usage
    sample_url = "https://api.github.com/users/zmlbrock"
    data = fetch_data(sample_url)
    print(f"Fetched data: {data}")
    
    if data:
        df = process_data([data])  # Wrap in list for DataFrame
        print(f"\nProcessed DataFrame:\n{df}")