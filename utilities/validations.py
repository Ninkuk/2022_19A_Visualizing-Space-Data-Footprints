#########################
# FILE INPUT VALIDATION #
#########################

# This list specifies the image extensions allowed for user file input
allowed_image_extensions = ["FITS", "XML"]

def allowed_image(filename):
    """Validate filename based on allowed file extensions.

    Args:
        filename (str): file name like test.fits or text.xml

    Returns:
        bool: Indicates whether the file name is valid or not.
    """

    # binary files not allowed
    if not '.' in filename:
        return False

    # extract extension from name
    file_ext = filename.split(".")[-1]

    # check if extension belongs in list of allowed file extensions
    if file_ext.upper() not in allowed_image_extensions:
        return False

    # return True if all validating checks pass
    return True