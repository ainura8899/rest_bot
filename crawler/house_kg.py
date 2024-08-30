import requests
from parsel import Selector
from pprint import pprint


class HouseCrawler:
    MAIN_URL = 'https://www.house.kg/snyat'
    BASE_URL = "https://www.house.kg"

    def get_page(self):
        page = requests.get(url=HouseCrawler.MAIN_URL, timeout=5)
        print(page.text[:400])
        self.page = page.text


    def get_house_links(self):
        html = Selector(text=self.page)
        links = html.css('p.title a::attr(href)').getall()
        links = list(map(lambda l: HouseCrawler.BASE_URL + l, links))
        return links[:3]
        pprint(links)

if __name__ == "__main__":
    crawler = HouseCrawler()
    crawler.get_page()
    crawler.get_house_links()


