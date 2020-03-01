# import os and ftplib module
import os
from ftplib import FTP, error_perm


def download_chirps_data():
    with FTP('ftp.chg.ucsb.edu')as ftp:  # connect to host ftp server
        print("\nConnecting to the server........")
        ftp.login()  # login to the ftp sever
        print("***Successfully connected****\n")
        # change the directory
        ftp.cwd('/pub/org/chg/products/CHIRPS-2.0/EAC_monthly/tifs/')
        print("Fetching data.........")
        file_names = ftp.nlst()  # list directory contents
        count = 0
        start_year = int(input("Enter the start year to download data:"))
        end_year = int(input("Enter the end year to download data:"))
        for filename in file_names:
            # download data between the year 1982 and 2018
            if get_year(filename) in range(start_year, end_year+1):
                count += 1
                host_file = os.path.join(os.getcwd(), filename)
                try:
                    with open(host_file, 'wb')as local_file:
                        print('downloading.....')
                        ftp.retrbinary('RETR ' + filename, local_file.write)
                        print("finished downloading", filename)
                        print("-------------------------------------------------")
                   
                except error_perm:
                    pass
        ftp.quit()
        print(count, "datasets downloaded\n\n\n")
        ftp.close()  # terminate the connection
        print("******************created by Evans***************")


def get_year(file_name):

    formatted_filename = file_name.replace("chirps-v2.0.", "")
    year = formatted_filename[0:4]
    return int(year)


download_chirps_data()
