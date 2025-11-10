import pandas as pd 
import numpy as np

from functions.convert_point import convert_point_28992_to_4326
from functions.utils.print_dataframe_info import print_dataframe_info

trash_dataframe = pd.read_csv("data/bijplaatsingen.csv", low_memory=False)
trash_dataframe = trash_dataframe[trash_dataframe['datum_waarneming'].astype(str).str.startswith('2025')]
trash_dataframe['geometrie_str'] = trash_dataframe['geometrie'].astype(str)
print_dataframe_info(trash_dataframe)

grouped_by_bin = trash_dataframe.groupby(["straatnaam"]).agg(
        totaal_schouwen=("straatnaam", "size"),
        aantal_niet_aplus=("crow_score", lambda x: (x != "A+").sum()),
        aantal_grofvuil=("grof", np.sum),
        stadsdeel=("gbd_stadsdeel_naam", "first"),
        postcode=("postcode", "first"),
        adres=("straatnaam", "first"),
        geometrie_origineel=("geometrie", "first"),
        dumpplek=("dumpplek", "first"),
        eerste_melding=("datum_waarneming", "min"),
        laatste_melding=("datum_waarneming", "max")
        ).reset_index()

converted_coords = grouped_by_bin['geometrie_origineel'].apply(
    convert_point_28992_to_4326
)

grouped_by_bin['lon'] = [coord[0] for coord in converted_coords]
grouped_by_bin['lat'] = [coord[1] for coord in converted_coords]

grouped_by_bin = grouped_by_bin.sort_values(
    by='totaal_schouwen', 
    ascending=False
)

print_dataframe_info(grouped_by_bin)

grouped_by_bin.to_csv("all_bins_2025.csv")

