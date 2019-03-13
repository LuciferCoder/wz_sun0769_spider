# -*- coding: utf-8 -*-
import scrapy
from ..items import YangguangItem


class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/report?page=30']

    def parse(self, response):
        # / tbody / tr / td / table / ~~ / tr
        tr_list = response.xpath('//div[@class="greyframe"]/table[2]/tr/td/table/tr')
        # print(tr_list)
        for tr in tr_list:
            items = YangguangItem()
            items["title"] = tr.xpath('./td[2]/a[2]/text()').extract_first()
            items["href"] = tr.xpath('./td[2]/a[2]/@href').extract_first()
            items["status"] = tr.xpath('./td[3]/span/text()').extract_first()
            items["name"] = tr.xpath('./td[4]/@text()').extract_first()
            items["publish_time"] = tr.xpath('./td[5]/text()').extract_first()
            # 获取连接内容
            yield scrapy.Request(
                url=items["href"],
                callback=self.parse_details,
                meta={"items": items}
            )
        next_url = response.xpath('//a[text()=">"]/@href').extract_first()
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )

    def parse_details(self, response):
        items = response.meta["items"]
        items["content_image"] = response.xpath('//div[9]/table[2]/tbody/tr[1]/td/div[1]/img/@src').extract()
        items["content_image"] = ["http://wz.sun0769.com" + i for i in items]
        items["content"] = response.xpath('//div[9]/table[2]/tr//text()').extract()
