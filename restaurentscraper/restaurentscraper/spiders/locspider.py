import scrapy


class LocspiderSpider(scrapy.Spider):
    name = "locspider"
    allowed_domains = ["yelp.com"]
    start_urls = ["https://yelp.com"]

    def parse(self, response):
        restaurents = response.css('lis.  border-color--default__09f24__NPAKY::text').get()
        for restaurent in restaurents:
            relative_url = response.css('a.css-19v1rkv::atte(href)').get()
            yield response.follow(book_url, callback=self.parse_rest_page)

        next_page = response.css('a.pagination-link-component__09f24__JRiQO css-ahgoya::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page_url, callback=self.parse)


    def parse_rest_page(self, response):

        yield{
            'url' : response.url ,
            'restaurent_name' : response.css('h1.css-1se8maq::text').get(),
            'reviews' : response.css('a.css-19v1rkv::text').get(),
            'phone_number' : response.css('p. css-1p9ibgf::text').get(),
            'address' : response.css('p. css-qyp8bo::text').get(),
            'page_link' : response.css('a.css-1idmmu3::attr(href)').get()
        }

