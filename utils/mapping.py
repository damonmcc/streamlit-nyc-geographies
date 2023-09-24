import geopandas as gpd
import leafmap.foliumap as leafmap

NYC_CENTER_COORDS = [40.726446, -73.983307]
NYC_CENTER_ZOOM = 12

def show_basic_map(geodata: gpd.GeoDataFrame, name: str):
    m = leafmap.Map(tiles='stamenterrain', center=NYC_CENTER_COORDS, zoom=NYC_CENTER_ZOOM)
    m.add_gdf(geodata, layer_name=name)
    m.to_streamlit(width=600, height=700)


# @st.cache_data(ttl=120)
def show_demo_map():
    m = leafmap.Map(tiles='stamenterrain', center=NYC_CENTER_COORDS, zoom=12)
    # url = "https://github.com/opengeos/leafmap/blob/master/examples/data/countries.geojson"
    # m.add_vector(url, fill_alpha=0.5, fill_color="lightblue")
    # cable_lines_geojson = 'https://raw.githubusercontent.com/opengeos/leafmap/master/examples/data/cable_geo.geojson'
    # boroughs_gejson = "data/nyc_borough_boundaries.geojson"
    boroughs_gejson = "https://data.cityofnewyork.us/api/geospatial/tqmj-j8zm?method=export&format=GeoJSON"
    m.add_geojson(boroughs_gejson, layer_name="Boroughs")
    m.to_streamlit(width=600, height=700)

    # filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
    # m = leafmap.Map(tiles='stamenterrain', center=[37, -99], zoom=3)
    # m.add_heatmap(filepath, latitude="latitude", longitude='longitude', value="pop_max", name="Heat map", radius=20)
    # m.to_streamlit(width=700, height=500, add_layer_control=True)
    # return m
