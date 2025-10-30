import pandas as pd 

from functions.create_folium_map import create_folium_map

bins_dataframe = pd.read_csv("all_bins.csv")
print(f"Now creating a map for {len(bins_dataframe)} bins...")

create_folium_map(bins_dataframe)
