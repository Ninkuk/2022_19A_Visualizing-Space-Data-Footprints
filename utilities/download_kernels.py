from ftplib import FTP


def download_from_timeframe(timeframe):
    ftp = FTP("naif.jpl.nasa.gov")
    ftp.login()

    kernels = ["spk", "ck"]
    
    for kernel in kernels:
        ftp.cwd(f"/pub/naif/pds/pds4/orex/orex_spice/spice_kernels/{kernel}/")

        files = ftp.nlst()

        count = 0
        for file in files:
            if timeframe in file and "_sc_" in file:
                count += 1
                print(f"Downloading... {file}")
                ftp.retrbinary(f'RETR {file}',
                            open(f"./kernels/{kernel}/{file}", 'wb').write)

    print(f"Downloaded {str(count)} files from this timeframe...")
    ftp.quit()
