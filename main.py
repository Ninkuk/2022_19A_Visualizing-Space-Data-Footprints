import spiceypy
from modules.SPICE.get_image_information import get_camera_type, get_timeframe

# arya's code -> list of 1000 vectors
## load MetaK with orx_ocams_v04.ti
### spice.furnsh("/content/orx_ocams_v04.ti")
## get boresight
### spice.getfov(-64360, 4)
## create vectors


# Get the image file name
img_name = input("Please enter the image file name: ")

# Get image information
[utc, data_time_frame] = get_timeframe(img_name, DEBUG=True)
camera_type = get_camera_type(img_name, DEBUG=True)

# ninad
# surface intercept

# METAKR = 'convtm'
# spiceypy.furnsh(MK.create_dynamic_meta_kernel(METAKR))

# print("\n\nMeta Kernel created...")

# print("\n\n\n====== RESULT ======")
# get_target_radii()
# get_target_position(utc)
# get_camera_attitude(utc)
