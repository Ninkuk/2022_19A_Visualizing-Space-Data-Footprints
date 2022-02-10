from bs4 import BeautifulSoup
import datetime

def get_timeframe(img_name):
    with open(f'./images/{img_name}.xml') as f:
        data = f.read()

    soup = BeautifulSoup(data, 'xml')
    time = soup.find('date_of_observation')
    print(f"\n\nImage Timestamp: {time.text}\n\n")

    dt = datetime.datetime.strptime(time.text, "%Y-%m-%dT%H:%M:%S.%fZ")
    timestamp = dt.timestamp()
    utc = str(datetime.datetime.utcfromtimestamp(timestamp))

    data_time_frame = str(dt.date())[2:-2].replace("-", "")
    return [utc, data_time_frame]