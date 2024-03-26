#! /usr/bin/env python

#
## Crawler

import requests
import re
from urllib.parse import urljoin


dmn = "hackthissite.org"

def request(uri):
    try:
        return requests.get("https://" + uri)
    except requests.exceptions.ConnectionError:
        pass


# Discover domain folders using wlist.txt
def disc_domain():
    with open ("./subdomain_file/wlist.txt", "r") as wlist:
        itera = 0
        start = 0
        started_point = 15
        for line in wlist:
                search = line.strip() + "." + dmn  ##line.strip() to remove spaces
                start += 1
                if start >= started_point:
                    print(search)
                    if request(search):
                        print("[*] Discovered subdomain ==>> " + search)
                    # itera += 1 ## For testing to make the for loop 50 iterations
                    # if itera == 50:
                    #     break


# Discover files and folders using f_and_d_wlist.txt
def disc_files_and_subdom():
     with open ("./subdomain_files/f_and_d_wlist.txt", "r") as wlist:
        itera = 0
        start = 0
        started_point = 0
        for line in wlist:
                search = dmn + "/" + line.strip()  ##line.strip() to remove spaces
                start += 1
                if start >= started_point:
                    print(search)
                    if request(search):
                        print("[*] Discovered file or dir ==>> " + search)
                    # itera += 1 ## For testing to make the for loop 50 iterations
                    # if itera == 50:
                    #     break
                        

def extract_uris(content_uri):
    href_links = re.findall('(?:href=")(.*?)"', content_uri)
    for uri_ in href_links:
        # urljoin transform uri like /news/views/727 to a full uri https://www.hackthissite.org/news/views/727,
        # and it leaves the other uri without modifications.
        uri_ = urljoin("https://www." + dmn, uri_)
        if (dmn in uri_):
            print(uri_)
     


def spider(): 
    response = request(dmn)
    # .decode('utf-8', 'ignore') is to transfor byte to string as response.content retrives
    # the website in byte format
    # print(response.content.decode('utf-8', "ignore"))
    extract_uris(response.content.decode('utf-8', "ignore"))



# disc_domain()
# disc_files_and_subdom()
spider()