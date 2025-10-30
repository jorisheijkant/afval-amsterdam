import pandas as pd 
import numpy as np

from functions.convert_point import convert_point_28992_to_4326
from functions.utils.print_dataframe_info import print_dataframe_info

trash_dataframe = pd.read_csv("data/bijplaatsingen_2.csv", low_memory=False)
trash_dataframe['geometrie_str'] = trash_dataframe['geometrie'].astype(str)
print_dataframe_info(trash_dataframe)

dumpings_only = trash_dataframe[trash_dataframe["crow_score"] != "A+"]

print_dataframe_info(dumpings_only)

grouped_by_bin = dumpings_only.groupby(["bag_openbareruimte_id"]).agg(
        totaal_bijplaatsingen=("bag_openbareruimte_id", "size"),
        aantal_grofvuil=("grof", np.sum),
        stadsdeel=("gbd_stadsdeel_naam", "first"),
        postcode=("postcode", "first"),
        adres=("straatnaam", "first"),
        geometrie_origineel=("geometrie", "first"),
        dumpplek=("dumpplek", "first"),
        aantal_handhavingen=("handhaving", np.sum)
        ).reset_index()

converted_coords = grouped_by_bin['geometrie_origineel'].apply(
    convert_point_28992_to_4326
)

grouped_by_bin['lon'] = [coord[0] for coord in converted_coords]
grouped_by_bin['lat'] = [coord[1] for coord in converted_coords]

grouped_by_bin = grouped_by_bin.sort_values(
    by='totaal_bijplaatsingen', 
    ascending=False
)

print_dataframe_info(grouped_by_bin)

grouped_by_bin.to_csv("all_bins.csv")

