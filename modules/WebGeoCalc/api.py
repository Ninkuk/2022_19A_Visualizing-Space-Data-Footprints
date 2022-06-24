# import sys
# import requests
# import json
# import time
import webgeocalc

# Read API documentation here: https://wgc2.jpl.nasa.gov:8443/webgeocalc/documents/api-info.html

calc = webgeocalc.Calculation(
    calculation_type="SURFACE_INTERCEPT_POINT",
    kernels="OSIRIS-REx",
    target="BENNU",
    target_frame="IAU_BENNU",
    shape_1="ELLIPSOID",
    reference_frame="IAU_BENNU",
    observer="ORX_OCAMS_MAPCAM",
    direction_vector_type="INSTRUMENT_FOV_BOUNDARY_VECTORS",
    direction_instrument="ORX_OCAMS_MAPCAM",
    aberration_correction='NONE',
    times="2019-09-23T09:01:13.548Z",
    state_representation="LATITUDINAL"
)

calc.submit()


def get_surface_intercepts(projection_vectors):
    # calc = webgeocalc.Calculation(
    #         calculation_type="SURFACE_INTERCEPT_POINT",
    #         kernels="OSIRIS-REx",
    #         target="BENNU",
    #         target_frame="IAU_BENNU",
    #         shape_1="ELLIPSOID",
    #         reference_frame="IAU_BENNU",
    #         observer="ORX_OCAMS_MAPCAM",
    #         direction_vector_type="VECTOR_IN_INSTRUMENT_FOV",
    #         direction_instrument="ORX_OCAMS_MAPCAM",
    #         direction_vector_x=projection_vectors[0][0],
    #         direction_vector_y=projection_vectors[0][1],
    #         direction_vector_z=projection_vectors[0][2],
    #         aberration_correction='NONE',
    #         times="2019-09-23T09:01:13.548Z",
    #         state_representation="LATITUDINAL"
    #     )

    # calc.submit()
    # sys.exit()

    # calculation_queue = []

    calc = webgeocalc.Calculation(
        calculation_type="SURFACE_INTERCEPT_POINT",
        kernels="OSIRIS-REx",
        target="BENNU",
        target_frame="IAU_BENNU",
        shape_1="ELLIPSOID",
        reference_frame="IAU_BENNU",
        observer="ORX_OCAMS_MAPCAM",
        direction_vector_type="INSTRUMENT_FOV_BOUNDARY_VECTORS",
        direction_instrument="ORX_OCAMS_MAPCAM",
        aberration_correction='NONE',
        times="2019-09-23T09:01:13.548Z",
        state_representation="LATITUDINAL"
    )

    calc.submit()
    # time.sleep(1)

    # print(calculation_queue)
    # time.sleep(5)

    # for index in range(len(calculation_queue)):
    #     if index % 10 == 0:
    #         time.sleep(5)
    #     calculation_id = calculation_queue[index]
    #     r = requests.get(
    #         f"https://wgc2.jpl.nasa.gov:8443/webgeocalc/api/calculation/{calculation_id}/results")
    #     print(r.json())
