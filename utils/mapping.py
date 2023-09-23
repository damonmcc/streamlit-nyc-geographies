import leafmap


def show_demo_map():
    m = leafmap.Map()
    url = 'https://github.com/opengeos/leafmap/blob/master/examples/data/countries.geojson'
    m.add_vector(url, fill_alpha=0.5, fill_color='lightblue')
    m