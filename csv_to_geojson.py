import pandas as pd
import json

df = pd.read_csv("all_bins.csv")

df.rename(columns={'lat': 'latitude', 'lon': 'longitude'}, inplace=True)

geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [float(row.longitude), float(row.latitude)]
            },
            "properties": {
                "id": row.get("id", i),
                **{col: row[col] for col in df.columns if col not in ["latitude", "longitude"]}
            },
        }
        for i, row in df.iterrows()
    ],
}

with open("all_bins.geojson", "w") as f:
    json.dump(geojson, f)

print("✅ Created all_bins.geojson with", len(df), "points")

