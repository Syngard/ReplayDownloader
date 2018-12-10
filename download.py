import urllib3, certifi
import json

from urllib.error import URLError
from urllib.parse import parse_qsl
from urllib.parse import quote
from urllib.parse import unquote
from urllib.parse import urlencode
from urllib.request import urlopen
from urllib import request

from menu import menu_choices 

class Downloader:
    def __init__(self, url):
        self.url   = url

    def start(self):
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
        
        # Get page from replay website
        resp = http.request('GET', self.url)

        # find API URL for the movie
        json_url = resp.data[resp.data.find(b'json_url')+9:]
        json_url = json_url[:json_url.find(b'"')]
        json_url = str(json_url)[2:-1]
        json_url = self.url_decode(json_url)
        
        # Get the json response from API
        json_file = http.request('GET', json_url)
        
        # Parse JSON response to use properly
        parsed    = json.loads(json_file.data)
        files     = parsed['videoJsonPlayer']['VSR']
        
        # Menu to choose language and resolution
        video_url = menu_choices(files)
        
        # Download video and write to file
    
    # Decode some URL-encoded characters in a URL
    # To be replaced by a lib function (in urllib most likely)
    def url_decode(self, url):
        n_url = ""
        i = 0
        while (i < len(url)):
            if (url[i] == '%'):
                n_url += chr(int('0x'+url[i+1:i+3], 16))
                i += 3
            else:
                n_url += url[i]
                i += 1
        
        return n_url





d = Downloader('https://www.arte.tv/fr/videos/052720-000-A/margin-call/')
d.start()
