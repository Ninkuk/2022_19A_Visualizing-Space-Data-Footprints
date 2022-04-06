import spiceypy
from modules.SPICE.get_image_information import get_timeframe


img_name = input("Please enter the image file name: ")

[utc, data_time_frame] = get_timeframe(img_name, DEBUG = True)


# arya's code -> list of 1000 vectors
    # API call: boresight, boundary vectors

# ninad
    # surface intercept

# print(get_timeframe(img_name))

# METAKR = 'convtm'
# spiceypy.furnsh(MK.create_dynamic_meta_kernel(METAKR))

# print("\n\nMeta Kernel created...")

# print("\n\n\n====== RESULT ======")
# get_target_radii()
# get_target_position(utc)
# get_camera_attitude(utc)
