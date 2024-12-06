#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 21:35:00 2024

@author: Jasmine Chen
"""

import requests
import pandas as pd

API_KEY = "45a9046a-12f7-4a26-ae9f-87073c5a6a0d"
LIMIT = "NONE"
REGION = "us-central"

def get_bereal_data(api_key, limit, region):
    '''
    Get BeReal data from the API for a specific region.

    Parameters:
        api_key (str): My API Key
        limit (str): Number of records to get per region (Default is "NONE")
        region (str): Region to get data for

    Returns:
        pd.DataFrame: DataFrame with BeReal moments for the specified region
    '''
    url = "https://bereal.devin.rest/v1/moments/all"
    params = {
        "api_key": api_key,
        "limit": limit,
        "format": "JSON"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()["regions"][region]

    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["utc"])
    return df

def main():
    bereal_data = get_bereal_data(API_KEY, limit=LIMIT, region=REGION)
    print(bereal_data)

if __name__ == "__main__":
    main()