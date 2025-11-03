import pandas as pd 

trash_dataframe = pd.read_csv("data/bijplaatsingen.csv", low_memory=False)
search_term = "Commelinstraat"
search_column = "straatnaam"

results_dataframe = trash_dataframe[trash_dataframe[search_column].str.contains(search_term, case=False, na=False)]

results_dataframe.to_csv("search_results.csv")
