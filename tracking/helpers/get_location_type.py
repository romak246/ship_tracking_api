import geopandas as gpd
from shapely.geometry import Point


def get_location_type(lat, lon):
    water_bodies = gpd.read_file('tracking/ne_10m_ocean.shp')
    point = Point(lon, lat)
    point_gdf = gpd.GeoDataFrame(geometry=[point], crs=water_bodies.crs)
    intersection = gpd.sjoin(point_gdf, water_bodies, how='inner', predicate='intersects')
    if intersection.empty:
        print('Координаты не являются водой')
    else:
        print('Координаты находятся в водной зоне')
    return False if intersection.empty else True
