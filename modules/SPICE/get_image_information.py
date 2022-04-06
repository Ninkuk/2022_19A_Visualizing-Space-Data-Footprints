# from main import DEBUG
from bs4 import BeautifulSoup
import datetime

def get_timeframe(img_name, DEBUG=False):
    """This function takes the image name and extracts the timestamp that it was taken at.

    Args:
        img_name (str): Image name with or without extension. Must have a corresponding xml file of the same name!

    Returns:
        list: Returns a list containing utc timestamp and the data time frame for downloading appropriate kernels.
    """

    with open(f'./images/{img_name}.xml') as f:
        data = f.read()

    soup = BeautifulSoup(data, 'xml')
    time = soup.find('date_of_observation')

    dt = datetime.datetime.strptime(time.text, "%Y-%m-%dT%H:%M:%S.%fZ")
    timestamp = dt.timestamp()
    utc = str(datetime.datetime.utcfromtimestamp(timestamp))

    data_time_frame = str(dt.date())[2:-2].replace("-", "")

    if DEBUG: print(f"Image Timestamp: {time.text}\nUTC: {utc}\nData Time Frame: {data_time_frame}")
    return [utc, data_time_frame]