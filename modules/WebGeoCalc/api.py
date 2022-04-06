import requests

# Read API documentation here: https://wgc2.jpl.nasa.gov:8443/webgeocalc/documents/api-info.html
api_url = "https://wgc2.jpl.nasa.gov:8443/webgeocalc/api"


def get(endpoint, headers):
    pass


def post(endpoint, headers, payload):
    response = requests.post(api_url + endpoint, json=payload)
    if response.ok:
        return response.json()

    return response.raise_for_status()


def get_kernel_set_id(id):
    pass