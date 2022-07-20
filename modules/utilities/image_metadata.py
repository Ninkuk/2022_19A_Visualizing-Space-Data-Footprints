def get_fits_image_metadata(file_header):
    """Returns a dictionary with all the fields required for calculations

    Args:
        file_header (header object): Header of a FITS file

    Returns:
        dict: dictionary with slect values from FITS header file
    """

    # check if header is valid
    if not file_header["SIMPLE"]:
        return None

    image_metadata = {
        # Length of data axis 1: 1024
        "x_axis_len": file_header["NAXIS1"],

        # Length of data axis 2: 1024
        "y_axis_len": file_header["NAXIS2"],

        # Mission: OSIRIS-REx
        "mission": file_header["MISSION"],

        # PDS terminology for spacecraft name: OREX
        "hostname": file_header["HOSTNAME"],

        # Instrument: OCAMS
        "instrument": file_header["INSTRUME"],

        # Target Object: BENNU
        "target": file_header["TARGET"],

        # Mission Phase: Recon
        "mission_phase": file_header["MPHASE"],

        # Spacecraft Clock String
        "sclk": file_header["SCLK_STR"],

        # [Sec] ocams_image_header.et
        "et": file_header["ET"],

        # Observation start YYYY-MM-DDThh:mm:ss.sss
        "date_obs": file_header["DATE_OBS"],

        # Object Name: BENNU
        "object": file_header["OBJECT"],

        # Boresight latitude of the imaging location
        "lat": file_header["LAT"],

        # Boresight longitude of the imaging location
        "lon": file_header["LON"],

        # ID of camera in use. 0- Map, 1-Sam, 2-Poly
        "camera_id": file_header["CAMERAID"],

        # ID that is associated with an image
        "image_id": file_header["IMAGEID"],

        # PolyCam NAIF Instrument ID
        "instrument_naif_id": file_header["PCNAIFID"]
    }

    return image_metadata


def get_xml_image_metadata(file_type):
    pass
