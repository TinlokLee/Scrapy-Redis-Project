from scrapy.item import Item, Field

class YouyuanItem(Item):
    header_url = Field()
    username = Field()
    monologue = Field()
    pic_url = Field()
    age = Field()
    source = Field()
    source_url = Field()
    crawled = Field()
    spider = Field()