# from functools import cached_property
import pandas as pd
import geopandas as gpd
from typing import Optional


WKT_PROJECTION = "EPSG:4326"
NYC_PROJECTION = "EPSG:2263"
DEFAULT_PROJECTION = NYC_PROJECTION

GEOGRAPHY_DETAILS = pd.read_csv("geography_details.csv").set_index("code")


class Geography:
    def __init__(
        self,
        name: str,
        code: str,
        url: str = None,
    ):
        self.name = name
        self.code = code
        self.url = url
        self.geometries = None

    def _get_geometries(self):
        geometries = gpd.read_file(self.url)
        if geometries.crs != DEFAULT_PROJECTION:
            geometries = reproject_geometry(geometries, DEFAULT_PROJECTION)
        self.geometries = geometries
    # TODO set columns of geometries (code, name, geometry)


def construct_all_geographies() -> dict[str, Geography]:
    geoegraphies = {}
    for details in GEOGRAPHY_DETAILS.itertuples():
        geoegraphies[details.Index] = Geography(
            name=details.name,
            code=details.Index,
            url=details.uri,
        )
    return geoegraphies


def fetch_geometries(geographies: list[Geography]):
    for geo in geographies.values():
        geo._get_geometries()


def reproject_geometry(
    data: gpd.GeoDataFrame,
    new_projection: str,
    old_projection: Optional[str] = None,
) -> gpd.GeoDataFrame:
    if not data.crs and not old_projection:
        raise RuntimeError(
            f"GeoDataFrame has no CRS set. Must declare one using the old_projection arg."
        )
    if old_projection:
        data.set_crs(old_projection, inplace=True)
    old_projection = data.crs
    data.to_crs(new_projection, inplace=True)
    if data.crs != new_projection:
        raise RuntimeError(
            f"Actual new projection {data.crs} is not the expected {new_projection}"
        )
    return data
