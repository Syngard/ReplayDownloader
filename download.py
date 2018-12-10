import urllib3
import json

class Downloader:
    def __init__(self, url):
        self.url   = url

    def start(self):
        http = urllib3.PoolManager()
        resp = http.request('GET', self.url)

        json_url = resp.data[resp.data.find(b'json_url')+9:]
        json_url = json_url[:json_url.find(b'"')]
        json_url = str(json_url)[2:-1]
        json_url = self.url_decode(json_url)
        
        json_file = http.request('GET', json_url)
        
        parsed    = json.loads(json_file.data)
        self.menu_choices(parsed)

    def url_decode(self, url):
        n_url = ""
        i = 0
        while (i < len(url)):
            if (url[i] == '%'):
                a = url[i+1:i+3]
                n_url += chr(int('0x'+a, 16))
                i += 3
            else:
                n_url += url[i]
                i += 1
        
        return n_url

    def menu_choices(self, parsed):
        for i in parsed['videoJsonPlayer']['VSR']:     
            print(parsed['videoJsonPlayer']['VSR'][i]['width'], 'x',
                    parsed['videoJsonPlayer']['VSR'][i]['height'], ';',
                  parsed['videoJsonPlayer']['VSR'][i]['versionLibelle'],'\n')


d = Downloader('https://www.arte.tv/fr/videos/052720-000-A/margin-call/')

d.start()
