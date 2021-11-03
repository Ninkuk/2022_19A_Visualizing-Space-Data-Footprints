import requests
from bs4 import BeautifulSoup
import os

# SPICE Kernels Archived Data: https://naif.jpl.nasa.gov/naif/data_archived.html

kernel_file_extensions = {
    "SPK": [".bsp", ".xsp"],
    "PcK": [".tpc", ".bpc", ".xpc"],
    "IK": [".ti"],
    "FK": [".tf"],
    "LSK": [".tls"],
    "CK": [".bc", ".xc"],
    "SCLK": [".tsc"],
    "MK": [".tm"],
    "DSK": [".bds"],
    "DBK": [".bdb", ".xdb"]
}


# This function asks the user to point to the kernel files on local machine
def local_kernel_input():
    return

def download_kernels(links):
    os.chdir('./kernels/')

    for link in links:
        req = requests.get(link)
        fileName = link.split("/")[-1]
        with open(fileName, 'wb') as f:
            f.write(req.content)

    return


def get_kernel_from_missions():
    print("\n\n\n")
    print("Available Missions")
    print("==================")

    url = "https://naif.jpl.nasa.gov/naif/data_archived.html"

    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'lxml')

    table = soup.find_all('table')[6]
    table_rows = table.find_all('tr')
    table_rows.pop(0)

    for idx, tr in enumerate(table_rows):
        td = tr.find_all('td')
        print("[" + str(idx + 1) + "] " + td[0].text)

    missionSelection = input("\nEnter your option: ")

    missionRow = table_rows[int(missionSelection) - 1]
    missionData = missionRow.find_all('td')

    missionLink = missionData[2].find('a')['href']
    missionPDS = int(missionData[3].text)

    if missionPDS == 3:
        missionLink += "/data/"
    elif missionPDS == 4:
        missionLink += "/spice_kernels/"
    else:
        "PDS not supported"


def get_kernels_from_links():
    print("\n\n\n")
    print("Manual File URL input")
    print("=====================")

    links = []

    while True:
        userInput = input("Enter a link or type 'exit': ")
        if userInput == 'exit':
            break
        else:
            links.append(userInput)
    
    download_kernels(links)

    return


def online_kernel_input():
    print("\n\n\n")
    print("Online Source")
    print("=============")
    print("You can find the PDS SPICE Archives here: https://naif.jpl.nasa.gov/naif/data_archived.html")
    print("\n")

    print("[1] Get kernels from available missions")
    print("[2] Manually paste the file URLs")
    sourceType = input("Enter your option: ")

    # TODO: data validation of sourceType (int)
    sourceType = int(sourceType)

    if sourceType == 1:
        get_kernel_from_missions()
    else:
        get_kernels_from_links()

    return


if __name__ == '__main__':
    print("Kernel Files Input")
    print("==================")

    print("[1] Get all files in /kernels/ directory")
    print("[2] Enter the path to kernels directory on local machine [DISABLED: Can only feasibly work with a gui file explorer]")
    print("[3] Get kernel files from an online source")
    inputType = input("Enter your option: ")

    # TODO: data validation of inputType (int)
    # inputType = int(inputType)

    online_kernel_input()
