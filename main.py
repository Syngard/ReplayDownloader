import json

from urllib.error import URLError
from urllib.parse import parse_qsl
from urllib.parse import quote
from urllib.parse import unquote
from urllib.parse import urlencode
from urllib.parse import unquote
from urllib.request import urlopen
from urllib import request

from menu import menu_choices 
from request import get
import download

class Arte:
    # Interface to download movies from the Arte website

    def __init__(self, url):
        self.url   = url

    def start(self):
        
        # Get page from replay website
        resp = get(self.url)

        # find API URL for the movie
        json_url = resp[resp.find('json_url')+9:]
        json_url = json_url[:json_url.find('"')]
        json_url = unquote(json_url) 
        
        # Get the json response from API
        json_f   = get(json_url)
        
        # Parse JSON response to use properly
        files     = json.loads(json_f)['videoJsonPlayer']['VSR']
        
        # Menu to choose language and resolution
        video_url = menu_choices(files)
        
        # Download video and write to file
        download(video_url) 



Arte('https://www.arte.tv/fr/videos/085341-000-A/fifo/').start()
