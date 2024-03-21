# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy_book.spiders.book_detail import BookDetailSpider


class ScrapyBookPipeline:
    def process_item(self, item, spider):
        if isinstance(spider, BookDetailSpider):
            return self.process_book_detail_item(item)
        adapter = ItemAdapter(item)
        adapter["price"] = float(adapter["price"][0][1:])
        adapter["image"] = "https://books.toscrape.com/" + adapter["image"][0]
        return item

    def process_book_detail_item(self, item):
        adapter = ItemAdapter(item)
        adapter["price"] = float(adapter["price"][0][1:])
        adapter["image"] = "https://books.toscrape.com/" + "/".join(adapter["image"][0].split("/")[2:])
        adapter["in_stock"] = int(adapter["in_stock"][0].split(" ")[2][1:])
        adapter["title"] = adapter["title"][0]
        adapter["description"] = adapter["description"][0]
        adapter["category"] = adapter["category"][0]
        
        return item
