from flask import Flask, render_template, request
from astropy.io import fits
from modules.main import get_results
# from main import xyz
from utilities.validations import allowed_image

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
                    # fits.getheader(files[0])["DATE"]

                    get_results(file)

        return request.url


if __name__ == "__main__":
    app.run(debug=True)
