import urllib3, certifi
import json

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
        self.menu_choices(files)

    
    # Decode some URL-encoded characters in a URL
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

    # Prints a menu and gets user choice for language/quality
    def menu_choices(self, files):
        versions, resolutions = [], []
        for i in files:
            ver = files[i]['versionLibelle']
            if ver not in versions:
                versions.append(ver)
                print(">>>", ver)

        chosen_version = input(">>> Choice : ")

        for i in files:
            res = (str(files[i]['width']),str(files[i]['height']))
            if (files[i]['versionLibelle'] == chosen_version
                            and res not in resolutions):
                resolutions.append(res)
                print(">>>", res[0]+"x"+res[1])

        choosen_res = input(">>> Choice : ").split('x')
        choosen_res = (int(choosen_res[0]), int(choosen_res[1]))

        # Finding the identifier for the right version 
        for i in files:
            if (files[i]['versionLibelle'] == chosen_version and
                (files[i]['width'],files[i]['height']) == choosen_res and
                files[i]['mediaType'] == "mp4"):
                video_id = i
                video_url = files[i]['url']
                break

        print(video_id,":",video_url)

d = Downloader('https://www.arte.tv/fr/videos/052720-000-A/margin-call/')
d.start()
