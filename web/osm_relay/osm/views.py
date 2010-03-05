from osm.utils import JSONResponse
from osm.parsers import get_streets


def relay(request):
    """
    Relays a request to OSM API, returns a JSON response
    """
    streets = get_streets(request.GET.get("bbox"))

    return JSONResponse("Streets parsed.", content={
        "streets": streets,
    })
