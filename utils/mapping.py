import leafmap


def show_demo_map():
    # m = leafmap.Map()
    # url = "https://github.com/opengeos/leafmap/blob/master/examples/data/countries.geojson"
    # m.add_vector(url, fill_alpha=0.5, fill_color="lightblue")

    filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
    m = leafmap.Map(tiles='stamenterrain', center=[37, -99], zoom=3)
    m.add_heatmap(filepath, latitude="latitude", longitude='longitude', value="pop_max", name="Heat map", radius=20)
    m.to_streamlit(width=700, height=500, add_layer_control=True)
    # return m
