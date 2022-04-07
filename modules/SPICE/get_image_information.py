from bs4 import BeautifulSoup
from utilities.time_conversion import convert_iso_to_utc, get_datetime_from_iso


def get_timeframe(img_name, DEBUG=False):
    """This function takes the image name and extracts the timestamp that it was taken at.

    Args:
        img_name (str): Image name with or without extension. Must have a corresponding xml file of the same name!

    Returns:
        list: Returns a list containing utc timestamp and the data time frame for downloading appropriate kernels.
    """

    # remove the extensions
    extensions = ["fits", "jpg", "png"]
    for extension in extensions:
        img_name = img_name.replace(f".{extension}", "")

    # open the xml file and read its content
    with open(f'./images/{img_name}.xml') as f:
        data = f.read()

    # parse the xml using bs4 and get the <date_of_observation></date_of_observation> tag
    soup = BeautifulSoup(data, 'xml')
    time = soup.find('date_of_observation')

    # get utc and create the data time frame
    utc = convert_iso_to_utc(time.text)
    data_time_frame = str(get_datetime_from_iso(time.text).date())[2:-2].replace("-", "")

    if DEBUG: 
        print(f"Image Timestamp: {time.text}\nUTC: {utc}\nData Time Frame: {data_time_frame}")
        
    return [utc, data_time_frame]


def get_camera_type(img_name, DEBUG=False):
    """Get the name of the camera that took the given image

    Args:
        img_name (str): image name with or without the extension
        DEBUG (bool, optional): Boolean flag to print debug output. Defaults to False.

    Returns:
        str: Camera type
    """

    # split the string using _ 
    camera_type = img_name.split("_")[1]

    if DEBUG:
        print(f"Camera type found: {camera_type}")

    return camera_type
