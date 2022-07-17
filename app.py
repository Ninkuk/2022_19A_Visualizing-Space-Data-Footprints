from flask import Flask, render_template, request
from astropy.io import fits
from main import xyz

app = Flask(__name__)


# Render index.html at website root
@app.route('/')
def index():
    return render_template('index.html')


# This list specifies the image extensions allowed for user file input
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["FITS", "XML"]


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
    if file_ext.upper() not in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return False

    # return True if all validating checks pass
    return True


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    # TODO: Add documentation

    # check form request type
    if request.method == "POST":
        
        # check if request contains file
        if request.files:

            # get the files as a list
            files = request.files.getlist("fileInput")

            # multiple file inputs - check each file
            for file in files:
                print(file)

                # empty file name not allowed
                if file.filename == "":
                    # TODO: return error view
                    print("Image must have a name")
                    return "Image must have a name"

                # check file extension
                if not allowed_image(file.filename):
                    # TODO: return error view
                    print("Image must be a .FITS or .XML file")
                    return "Image must be a .FITS or .XML file"

                # parse fits file header and pass information to backend
                if file.filename.lower().endswith(".fits"):
                    fits.getheader(files[0])["DATE"]

                    xyz(file)

        return request.url


if __name__ == "__main__":
    app.run(debug=True)
