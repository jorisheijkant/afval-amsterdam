from pyproj import Transformer
from shapely.wkt import loads

def convert_point_28992_to_4326(point_wkt):
    transformer = Transformer.from_crs("epsg:28992", "epsg:4326", always_xy=True)
    
    try:
        point_obj = loads(point_wkt)
        x_28992 = point_obj.x
        y_28992 = point_obj.y
        
        lon_4326, lat_4326 = transformer.transform(x_28992, y_28992)
        
        return lon_4326, lat_4326
    except Exception as e:
        print(f"Error during point conversion: {e}")
        return None, None
