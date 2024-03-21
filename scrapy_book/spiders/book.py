import scrapy
from scrapy_book.items import BookItem

class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css("article.product_pod")
        for book in books:
            book_item = BookItem()
            
            book_item["title"] = book.css("h3 a::attr(title)").get()
            book_item["price"] = book.css(".price_color::text").get(),
            book_item["image"] = book.css("img::attr(src)").get(),
            yield book_item
        next_page = response.css("li.next a::attr(href)").get()
        
        if next_page is not None:
            yield response.follow(next_page, self.parse)
