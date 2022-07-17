from flask import Flask, render_template, request
from astropy.io import fits
from modules.main import get_results
from utilities.validations import allowed_image
from utilities.image_metadata import get_fits_image_metadata, get_xml_image_metadata

app = Flask(__name__)


# Render index.html at website root
@app.route('/')
def index():
    return render_template('index.html')


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    # TODO: Add documentation

    # check form request type
    if request.method == "POST":
        print("POST method found")

        # check if request contains file
        if request.files:
            print("File(s) found in request")

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

                # pass file information to the backend
                image_metadata = get_fits_image_metadata(fits.getheader(file)) if file.filename.endswith("fits") else get_xml_image_metadata(file)
                get_results(image_metadata)

        return request.url


if __name__ == "__main__":
    app.run(debug=True)
