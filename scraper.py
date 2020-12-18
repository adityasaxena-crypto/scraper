import requests
import os
class Unsplash:
    def __init__(self,search_term,per_page=50,quality="raw"):
        self.search_term = search_term
        self.per_page = per_page
        
        self.quality = quality
        self.headers = {
            "Accept":	"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":	"gzip, deflate, br",
            "Accept-Language":	"en-US,en;q=0.5",
            "Host":	"unsplash.com",
            "User-Agent":	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"
         }

    def set_url(self):
        return f" https://unsplash.com/napi/search?query={self.search_term}&per_page={self.per_page}&xp=feedback-loop-v2%3Aexperiment"
    

    def make_request(self):
        url = self.set_url()
        return requests.request("GET",url,headers=self.headers)

    def get_data(self):
        self.data = self.make_request().json()
        
    

    

    

    def Scrapper(self,pages):
        for page in range(1):
            self.make_request()
            self.get_data()
            for item in self.data['photos']['results']:
                name = item['id']
                url = item['urls'][self.quality]
                with open(name+".jpg","wb") as f:
                 f.write(requests.get(url).content)
            

if __name__ == "__main__":
    scrapper = Unsplash("butterfly")
    scrapper.Scrapper(1)

    
