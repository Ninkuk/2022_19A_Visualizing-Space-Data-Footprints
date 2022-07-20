import requests
import zipfile
import os


def download_subset_kernels(subset_dir_path):
    """Download kernels from the list of URLs provided by the subset folder

    Args:
        subset_dir_path (str): path to the subset folder
        kernel_dir_path (str): path to the kernel folder within subset
    """
    # TODO: Implement exceptions

    # get the txt file containing urls
    urls_file = [file
                 for file in os.listdir(subset_dir_path)
                 if file.endswith(".txt") and file.startswith("url")][0]

    # read all the urls in the file
    with open(os.path.join(subset_dir_path, urls_file), 'r') as f:
        urls = f.read().splitlines()

    # download files via request
    for url in urls:
        # construct the file path to its respective kernel folder
        file_path = os.path.join(
            './kernels',
            url.split('/')[-2],
            url.split('/')[-1]
        )

        # only download new files
        if not os.path.isfile(file_path):
            file_response = requests.get(url)
            with open(file_path, 'wb') as f:
                f.write(file_response.content)


def download_subset(mission_path, time_start, time_stop=""):
    """Download the kernel subset folder based on the given timeframe

    Args:
        mission_path (str): Path to the PDS4 mission archive data in the NAIF server
        time_start (str): Time from fits header
        time_stop (str, optional): Stop time for subset. Defaults to "".

    Returns:
        str: Kernel directory path if method is successfully run
    """

    # TODO: Implement exceptions

    # URL for NAIF Archive data subset https://naif.jpl.nasa.gov/cgi-bin/subsetds.pl?dataset=orex/orex_spice
    url = "https://naif.jpl.nasa.gov/cgi-bin/subsetds.pl"

    # request parameters
    payload = {
        "dataset": mission_path,
        "start": time_start,
        "stop": time_stop,
        "action": "Subset"
    }

    # Make the call. This might take up to 20 seconds.
    response = requests.get(url, params=payload)

    # Process the response

    ###########################
    ## Step 1: Save zip file ##
    ###########################

    # root data directory
    data_directory = "./kernels"

    # Get zip file name and path from response header
    zip_file_name = response.headers["Content-disposition"].split(
        "=")[-1]
    zip_file_path = os.path.join(data_directory, zip_file_name)

    # Save zip file in kernels folder in chunks
    with open(zip_file_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=16*1024):
            f.write(chunk)

    ###################
    ## Step 2: Unzip ##
    ###################

    # Create new directory
    subset_dir_name = zip_file_name.removesuffix(".zip")
    subset_dir_path = os.path.join(data_directory, subset_dir_name)
    os.makedirs(subset_dir_path)

    # Unzip to new directory
    with zipfile.ZipFile(zip_file_path, 'r') as zip_f:
        zip_f.extractall(subset_dir_path)

    ########################
    ## Step 3: Delete zip ##
    ########################

    os.remove(zip_file_path)

    #############################
    ## Step 4: Download subset ##
    #############################

    download_subset_kernels(subset_dir_path)

    return subset_dir_path


if __name__ == "__main__":
    download_subset("orex/orex_spice", "2019-10-26T21:01:54.620")
