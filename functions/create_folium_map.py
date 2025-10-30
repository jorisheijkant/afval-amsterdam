import folium

def create_folium_map(dataframe):
    center_lat = dataframe['lat'].mean()
    center_lon = dataframe['lon'].mean()
    
    folium_map = folium.Map(location=[center_lat, center_lon], zoom_start=12, tiles="cartodbpositron")

    for index, row in dataframe.iterrows():
        popup_text = f"""
            <b>Address:</b> {row['adres']} ({row['postcode']})<br>
            <b>Total Dumpings:</b> {int(row['totaal_bijplaatsingen'])}<br>
            <b>Grofvuil:</b> {int(row['aantal_grofvuil'])}<br>
            <b>Stadsdeel:</b> {row['stadsdeel']}
        """

        if row['totaal_bijplaatsingen'] > dataframe['totaal_bijplaatsingen'].quantile(0.8):
            marker_color = 'red'
        elif row['totaal_bijplaatsingen'] > dataframe['totaal_bijplaatsingen'].quantile(0.5):
            marker_color = 'orange'
        else:
            marker_color = 'blue'

        folium.Marker(
            location=[row['lat'], row['lon']],
            popup=folium.Popup(popup_text, max_width=300),
            icon=folium.Icon(color=marker_color, icon='trash', prefix='fa')
        ).add_to(folium_map)

        map_filename = "map/containers.html"
        folium_map.save(map_filename)
