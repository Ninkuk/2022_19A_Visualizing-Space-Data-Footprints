from modules.WebGeoCalc.api import post
from utilities.api_utilities import create_json_dict, process_response


# Read API documentation here: https://wgc2.jpl.nasa.gov:8443/webgeocalc/documents/api-info.html#SURFACE_INTERCEPT_POINT
def get_surface_intercept_point():
    """
    This function gets the intercept point
    """

    # create JSON dict
    payload = create_json_dict()

    # pass and call api
    response = post("/calculations/new/", payload=payload)

    # process returned data
    process_response(response)
