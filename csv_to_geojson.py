import pandas as pd
import json

df = pd.read_csv("all_bins_2025.csv")

df.rename(columns={'lat': 'latitude', 'lon': 'longitude'}, inplace=True)

df = df.dropna(subset=['latitude', 'longitude'])

df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')

df = df.where(pd.notnull(df), None)

features = []
for _, row in df.iterrows():
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [float(row.longitude), float(row.latitude)],
        },
        "properties": {
            "Adres": row.get("adres"),
            "Aantal keer bijgeplaatst afval aangetroffen": row.get("aantal_niet_aplus"),
            "Totaal aantal schouwen": row.get("totaal_schouwen"),
            "Aantal keer grofvuil aangetroffen": row.get("aantal_grofvuil")
        },
    }
    features.append(feature)

geojson = {"type": "FeatureCollection", "features": features}

with open("all_bins_2025.geojson", "w") as f:
    json.dump(geojson, f, allow_nan=False)

print(f"✅ Saved 'trash_bins.geojson' with {len(features)} valid features and only selected properties")

