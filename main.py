import sys
import spiceypy
import numpy as np
from modules.SPICE.get_image_information import get_camera_type, get_timeframe
from modules.WebGeoCalc.api import get_surface_intercepts
from utilities.download_kernels import download_from_timeframe
from utilities.meta_kernel import create_dynamic_meta_kernel
from utilities.time_conversion import convert_utc_to_et
from utilities.vector_generation import get_mapcam_vectors, get_polycam_vectors

# get_surface_intercepts(projection_vectors_map)

# # Get the image file name


# Get image information
[utc, data_time_frame] = get_timeframe(img_name="20190922T010113S012_map_iofL2pan", DEBUG=True)
camera_type = get_camera_type(img_name="20190922T010113S012_map_iofL2pan", DEBUG=True)

download_from_timeframe(data_time_frame)
METAKR = 'convtm'
spiceypy.furnsh(create_dynamic_meta_kernel(METAKR))
print("[STATUS UPDATE]: Meta Kernel created...")

# Get the camera fov projection vectors at the start of the program
projection_vectors_map = get_mapcam_vectors()
projection_vectors_poly = get_polycam_vectors()
print("[STATUS UPDATE]: Projection Vectors Generated...")

print(projection_vectors_map)

# set observer frame based on camera type
if camera_type == "map":
    observer = "ORX_OCAMS_MAPCAM"
elif camera_type == "pol":
    observer = "ORX_OCAMS_POLYCAM"
else:
    observer = "ORX_OCAMS_SAMCAM"

# call surface intercept - API``
with spiceypy.no_found_check():
    print(spiceypy.sincpt(method="ELLIPSOID", target="BENNU", et=convert_utc_to_et(utc), fixref="IAU_BENNU", abcorr="NONE", obsrvr="-64361", dref="ORX_OCAMS_MAPCAM", dvec=np.array([0.006911283744662688, 0.006911283744662688, 0.9999522330161584])))

# multiple_points_to_csv - utility


# print("\n\n\n====== RESULT ======")
# get_target_radii()
# get_target_position(utc)
# get_camera_attitude(utc)
