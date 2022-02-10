from ftplib import FTP


def download_from_timeframe(timeframe):
    ftp = FTP("naif.jpl.nasa.gov")
    ftp.login()

    ftp.cwd("/pub/naif/pds/pds4/orex/orex_spice/spice_kernels/spk/")

    files = ftp.nlst()

    count = 0
    for file in files:
        if timeframe in file:
            count += 1
            print(f"Downloading... {file}")
            ftp.retrbinary(f'RETR {file}',
                           open(f"./kernels/spk/{file}", 'wb').write)

    print(f"Downloaded {str(count)} files from this timeframe...")
    ftp.quit()
