import winsdk.windows.devices.geolocation as wdg
import asyncio
from typing import NamedTuple


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


async def get_coords() -> Coordinates:
    locator = wdg.Geolocator()
    pos = await locator.get_geoposition_async()
    return Coordinates(latitude=pos.coordinate.latitude, longitude=pos.coordinate.longitude)


def get_location() -> Coordinates:
    try:
        return asyncio.run(get_coords())
    except PermissionError:
        print("ERROR: You need to allow applications to access you location in Windows settings")


print(get_location())
