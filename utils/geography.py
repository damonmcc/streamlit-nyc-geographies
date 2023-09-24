from functools import cached_property
import geopandas as gpd
# import streamlit as st
# import census
# from collections import namedtuple

# GEOGRAPHY_TYPES = [
#     ""
# ]

# name, code, type
# TestDataset = namedtuple(
#     "TestDataset",
#     [
#         "name",
#         "code",
#         "type",
#     ],
# )

class Geography():
    def __init__(
            self,
            name:str,
            code:str,
            url:str,
            # geometries:[gpd.GeoDataFrame],
    ):
        self.name = name
        self.code = code
        self.url = url
        self.geometries = gpd.read_file(self.url)
        # self.geometries = gpd.GeoDataFrame()
    
    # def _get_geometries(self) -> gpd.GeoDataFrame:
    #     return gpd.read_file(url)

    # @cached_property
    # def total_area() -> float:
        
        # for geometry in 
# "Borough, boro, 5, NYS, 2000 B.C.E, pretty big"
# GEOGRAPHIES = [
#     Geog(Borough

GEOEGRAPHIES = [
    Geography(name="Borough", code="boro", url="https://data.cityofnewyork.us/api/geospatial/tqmj-j8zm?method=export&format=GeoJSON",)
]


# def list_all_geographies():
    # """Showing the code of the demo."""
    # show_code = st.sidebar.checkbox("Show code", False)
    # if show_code:
        # Showing the code of the demo.
        # st.markdown("## Code")
        # sourcelines, _ = inspect.getsourcelines(demo)
        # st.code(textwrap.dedent("".join(sourcelines[1:])))
