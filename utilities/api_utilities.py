import json


def create_json_dict(
    calculation_type,
    times,
    targetFrame,
    observer,
    id=30,
    target="BENNU",
    directionVectorType="VECTOR_IN_INSTRUMENT_FOV",
    directionInstrument="",
    stateRepresentation="LATITUDINAL",
):

    # Load the json template and parse it into a dict
    with open('utilities/template_post_data.json') as f:
        template = json.loads(f.read())

    # Set parameter values in the dictionary
    template["kernels"][0]["id"] = id
    template["times"] = times
    template["calculationType"] = calculation_type
    template["target"] = target
    template["targetFrame"] = targetFrame
    template["observer"] = observer
    template["directionVectorType"] = directionVectorType
    template["directionInstrument"] = directionInstrument
    template["stateRepresentation"] = stateRepresentation

    return template


def process_response(response):
    pass


if __name__ == "__main__":
    create_json_dict()
