import pandas as pd


def print_me():
    print("Hello World")
    return True


def read_csv():
    df = pd.read_csv("sample.csv")
    print(df)
    return df