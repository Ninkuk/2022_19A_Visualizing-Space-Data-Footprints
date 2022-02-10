import spiceypy
from utilities.download_kernels import download_from_timeframe
from modules.get_image_information import get_timeframe
import utilities.meta_kernel as MK
from modules.get_target_information import get_target_position, get_target_radii

import sys

# sys.exit()

img_name = input("Please enter the image file name: ")

[utc, data_time_frame] = get_timeframe(img_name)
download_from_timeframe(data_time_frame)

METAKR = 'convtm'
spiceypy.furnsh(MK.create_dynamic_meta_kernel(METAKR))

print("\n\nMeta Kernel created...")

print("\n\n\n====== RESULT ======")
get_target_radii()
get_target_position(utc)
