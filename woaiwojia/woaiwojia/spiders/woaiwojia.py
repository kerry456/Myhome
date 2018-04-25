'''
auth:hexl
'''
import scrapy
import re

from woaiwojia.items import WoaiwojiaItem

from woaiwojia.items import Woaiwojia_detail_Item


class Woaiwojia_spider(scrapy.Spider):
    name = 'woaiwojia'
    # allowed_domains = 'bj.5i5j.com'
    base_url = 'https://bj.5i5j.com/zufang/n%s/'
    url_list = []
    for i in range(1,300):
        url = base_url%i
        url_list.append(url)
    start_urls = url_list

    def parse(self, response):
        item = WoaiwojiaItem()
        title_list = response.xpath('//h3[@class="listTit"]/a/text()').extract()
        area_list = re.findall('厅  ·  (.*?)  平米',response.text)
        price_list = response.xpath('//div[@class="jia"]/p[1]/strong/text()').extract()
        rent_method_list = response.xpath('//div[@class="jia"]/p[2]/text()').extract()
        url_list = response.xpath('//h3[@class="listTit"]/a/@href').extract()
        address_list = response.xpath('//div[@class="listX"]/p[2]/a/text()').extract()
        for title,area,price,rent_method,address,url in zip(title_list,area_list,price_list,rent_method_list,address_list,url_list):
            item['title'] = title
            item['area'] = area
            item['price'] = price
            item['rent_method'] = rent_method.replace('出租方式：','')
            item['address'] = address
            item['url'] = 'https://bj.5i5j.com'+url
            # yield item
            yield scrapy.Request(item['url'],callback=self.parse_detail,meta={'title':title})

    def parse_detail(self,response):
        item =Woaiwojia_detail_Item()
        item['title'] = response.meta['title']
        item['rent'] = response.xpath('//div[@class="housesty"]/div[1]/div/p[1]/text()').extract_first()
        item['floor'] = response.xpath('//div[@class="zushous"]/ul/li[2]/text()').extract_first()
        item['house_type'] = response.xpath('//div[@class="housesty"]/div[2]/div/p[1]/text()').extract_first()
        item['area'] = response.xpath('//div[@class="housesty"]/div[3]/div/p[1]/text()').extract_first()
        item['payment_method'] = response.xpath('//div[@class="housesty"]/div[4]/div/p[1]/text()').extract_first()
        #item['build_year'] = response.xpath('//div[@class="zushous"]/ul/li[6]/text()').extract_first()
        item['build_year'] = response.xpath('//div[@class="content fr"]/div[2]/ul/li[6]/text()').extract_first()
        item['rent_method'] = response.xpath('//div[@class="zushous"]/ul/li[7]/text()').extract_first()
        item['subway'] = response.xpath('//div[@class="zushous"]/ul/li[10]/text()').extract_first()
        item['contact'] = response.xpath('//div[@class="daikansty"]/ul/li[2]/h3/a/text()').extract_first()
	    #item['contact'] = response.xpath('//div[class="daikansty"]/ul/li[2]/h3/a/text()').extract_first()
        item['telephone_number'] = response.xpath('//div[@class="content fr"]/div[3]/ul/li[2]/label/text()').extract_first()
        return item






