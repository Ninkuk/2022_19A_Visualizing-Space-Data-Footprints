import spiceypy
import os
from modules.utilities.download_kernels import download_subset


def get_results(image_metadata=""):

    ##############################
    ## Step 1: Download kernels ##
    ##############################

    # You can find the PDS4 mission path here: https://naif.jpl.nasa.gov/pub/naif/pds/pds4/

    # Download the subset and its kernels
    subset_dir_path = download_subset(
        "orex/orex_spice", image_metadata["date_obs"])

    #########################
    ## Step 2: Meta kernel ##
    #########################

    # Get meta kernel file from subset dir
    
    # change directory to subset dir
    os.chdir(subset_dir_path)
    
    # find meta kernel (.tm) file in dir
    for file in os.listdir(os.getcwd()):
        if file.endswith(".tm"):
            meta_kernel = file
            break

    # furnsh meta kernel
    spiceypy.furnsh(meta_kernel)


if __name__ == "__main__":
    get_results()
