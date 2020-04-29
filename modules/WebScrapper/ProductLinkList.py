import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


class ScrapCatalogProductBoxes():

    url = ''
    scrap_result = []

    def __init__(self,url,css_product_box_selector):
        self.url = url
        self.css_product_box_selector = css_product_box_selector
        self.scrap()

    def headers(self):
        headers = requests.utils.default_headers()
        headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
        return headers

    def download_url_html(self):
        req = requests.get(self.url, self.headers() )
        #print(req.content)
        return req.content

    def scrap(self):

        if self.url and self.css_product_box_selector:
            soup = BeautifulSoup( self.download_url_html(), 'html.parser')
            self.scrap_result = soup.find_all( class_=self.css_product_box_selector )
            
        return self

    def result(self):
        return self.scrap_result




""" Extracts image, name and link from a product box """
class ProductCatalogBoxAssetExtractor():

    def __init__(self, box, domain):
        self.box = box
        self.domain = domain


    def full_url(self, link):
        return urljoin(self.domain, link )


    def image(self):
        return self.full_url(self.box.find_all("img")[0]["src"])


    def name(self, selector = None):


        if selector:
            return self.box.find_all( class_=selector )[0].string

        if self.box.title:
            return self.box.title

        return self.box.find_all("a")[1].text

    def link(self):
        return self.full_url(self.box.find_all("a")[1]["href"])



""" Extract Domain from scrapped URL """
class UrlDomainExtractor():
    
    domain = ''
    
    def __init__(self, url):
        self.url = url

    def get_domain(self):
        parsed_uri = urlparse(self.url)
        return '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
"""     


if __name__ == "__main__":

    payload = {
    "baseurl" : "http://www.sargentchile.cl/agricola/tractores/",
    "css_selector" : "card",
    "name_css_selector" : "card-title"
}

results = []

    Scrapper = ScrapCatalogProductBoxes(payload["baseurl"], payload["css_selector"])

    for box in Scrapper.result():

        # Domain FQDN
        site_domain = UrlDomainExtractor(payload["baseurl"])
        
        # Assets of interest
        Assets = ProductCatalogBoxAssetExtractor( box, site_domain.get_domain() )

        results.append({
            "image_url" : Assets.image(),
            "name" : Assets.name( payload["name_css_selector"] ),
            "link" : Assets.link(),
        })


    print (results) """