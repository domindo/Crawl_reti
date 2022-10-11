import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AllProjectSpider(CrawlSpider):
    name = 'all_project'
    allowed_domains = ['reti.vn']
    start_urls = ['https://reti.vn/projects']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='card card-media-768 col-4 items d-flex']/div/div[@class='owl-carousel owl-theme slide-card']/a[1]"),
             callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="(//li/a[@rel='next'])[2]"))
    )

    def parse_item(self, response):
        yield {
            'Tên dự án': response.xpath("//div[@class='info-department']/h3/text()").get(),
            'Địa chỉ': response.xpath("//div[@class='info-department']/span/text()").get(),
            'Giá bán': response.xpath("//div[@class='info-department']/div/span[2]/text()").get(),
            'Diện tích': response.xpath("//div[@class='info-department']/div/div/div[@class='acreage col-6 pl-0 ml-0']/span/text()").get().replace('\n', ''),
            'Chủ đầu tư': response.xpath("//div[@class='info-department']/div/div[1]/div[@class='sun-group col-6']/span/text()").get().replace('\n', ''),
            'Bàn giao': response.xpath("//div[@class='info-department']/div/div[2]/div[@class='sun-group col-6']/span/text()").get(),
            'Kiểu': response.xpath("//div[@class='info-department']/div/div/div[@class='apartment col-6 pl-0 ml-0']/span/text()").get(),
            'Phân khu': response.xpath("(//div[@class='info-department']/div/div/div[@class='floor col-6']/span[2]/text())[1]").get(),
            'Số căn': response.xpath("(//div[@class='info-department']/div/div[2]/div[@class='floor col-6']/span[2]/text())[1]").get(),
            'url': response.url
        }
