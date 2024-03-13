#! /usr/bin/env python

#
## Crawler

import requests

dmn = "hackthissite.org"

def request(uri):
    try:
        return requests.get("https://" + uri)
    except requests.exceptions.ConnectionError:
        pass


def disc_domain():
    with open ("./subdomain_file/wlist.txt", "r") as wlist:
        itera = 0
        start = 0
        started_point = 15
        for line in wlist:
                search = line.strip() + "." + dmn
                start += 1
                if start >= started_point:
                    print(search)
                    if request(search):
                        print("[*] Discovered subdomain ==>> " + search)
                    # itera += 1
                    # if itera == 50:
                    #     break


def disc_files_and_subdom():
     with open ("./subdomain_files/f_and_d_wlist.txt", "r") as wlist:
        itera = 0
        start = 0
        started_point = 0
        for line in wlist:
                search = dmn + "/" + line.strip()
                start += 1
                if start >= started_point:
                    print(search)
                    if request(search):
                        print("[*] Discovered file or dir ==>> " + search)
                    # itera += 1
                    # if itera == 50:
                    #     break


def spider(): 
    response = request(dmn)
    print(response.content)


# disc_domain()
# disc_files_and_subdom()
spider()