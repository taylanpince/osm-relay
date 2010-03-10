from lxml import etree


OSM_API_URL = "http://api.openstreetmap.org/api/0.6/map?bbox=%s"


def get_streets(bbox):
    """
    Makes an OSM API request and parses the streets and their waypoints in the
    XML response, returns a list
    """
    tree = etree.parse(OSM_API_URL % bbox)
    streets = []
    count = 0

    for way in tree.xpath("//way"):
        if len(way.xpath("tag[@k='highway']")) == 0:
            continue

        count += 1
        waypoints = []

        for node in way.getchildren():
            if node.tag == "nd":
                point = tree.xpath("//node[@id=%s]" % node.attrib.get("ref"))[0]

                waypoints.append((point.attrib.get("lat"), point.attrib.get("lon")))

        streets.append({
            "coordinates": waypoints,
            "rules": [
                {
                    "type": 1,
                    "days": ["Monday", "Tuesday"],
                    "start_time_hour": 7,
                    "start_time_minute": 0,
                    "end_time_hour": 17,
                    "end_time_minute": 0,
                },
                {
                    "type": 2,
                    "days": ["Thursday"],
                    "start_time_hour": 18,
                    "start_time_minute": 0,
                    "end_time_hour": 19,
                    "end_time_minute": 0,
                },
            ],
        })

        if count > 50: break

    return streets
