import importlib.resources

import pandas as pd


def print_me():
    print("Hello World")
    return True


def read_csv():
    data_path = importlib.resources.files("widget")
    df = pd.read_csv(str(data_path / "sample.csv"))
    print(df)
    return df
