import scrapy

from scrapy_book.items import BookDetailItem


class BookDetailSpider(scrapy.Spider):
    name = "book_detail"
    allowed_domains = ["books.toscrape.com"]
    # start_urls = ["https://books.toscrape.com"]
    start_urls = [
        "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"
    ]

    def parse(self, response):
        # books = response.css("article.product_pod")
        # for book in books:
        #     detail_page = book.css("h3 a::attr(href)").get()
        #     yield response.follow(detail_page, self.parse_book_detail)

        # next_page = response.css("li.next a::attr(href)").get()

        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
        book_info_keys = map(lambda x: x.strip().replace(" ", "_").lower().replace(".", "").replace("(", "").replace(")", ""), response.css("table.table th::text").getall())
        book_info_values = response.css("table.table td::text").getall()
        book_info = dict(zip(book_info_keys, book_info_values))
        yield book_info

    def parse_book_detail(self, response):
        def extract_with_css(query):
            return response.css(query).get().strip()

        # book_details = BookDetailItem()
    
        # book_details["title"] = extract_with_css("div.product_main h1::text"),
        # book_details["price"] = extract_with_css("div.product_main p.price_color::text"),
        # book_details["image"] = extract_with_css("div.thumbnail div.item img::attr(src)"),
        # book_details["in_stock"] = response.xpath("//*[@id='content_inner']/article/div[1]/div[2]/p[2]/text()")[1].get().strip(),
        # book_details["category"] = response.xpath("//*[@id='default']/div/div/ul/li[3]/a/text()").get(),
        # book_details["description"] = response.xpath("//*[@id='content_inner']/article/p/text()").get(),
        # yield book_details
        book_info = response.css("table.table")
        print(book_info)
        yield {}
