import pandas as pd

def save_first_rows(dataframe, amount_of_rows=10):
    first_rows = dataframe.head(amount_of_rows)
    first_rows.to_csv("first_rows.csv")

