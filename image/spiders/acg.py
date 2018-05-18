# -*- coding: utf-8 -*-
import scrapy
import json
import re
from image.items import ImageItem

class AcgSpider(scrapy.Spider):
    name = 'acg'
    allowed_domains = ['acg.fi','gov.com']
    # start_urls = ['http://acg.fi/']
    # 抓包,发现是换页是发送的post请求
    def start_requests(self):
        item = ImageItem()
        post_url = 'http://www.acg.fi/wp-admin/admin-ajax.php?action=zrz_load_more_posts'
        # 分析参数
        dic = {
            '1' : ['anime',25],
            '2' : ['hentai',31],
            '3' : ['yusanjia',18],
            '4' : ['zhifu',34],
            '5' : ['zatuji',50],
            '507' : ['fuli',8]
        }
        for k,v in dic.items():
            headers = {
                'Accept': 'application / json, text / plain, * / *',
                'Accept - Language': 'zh - CN, zh;q = 0.9',
                'Connection': 'keep - alive',
                'Content - Length': '18',
                'Content - Type': 'application / x - www - form - urlencoded',
                # 'Cookie': '_ga=GA1.2.2078460723.1526562976; _gid=GA1.2.1345011025.1526562976',
                'Host': 'www.acg.fi',
                'Origin': 'http: // www.acg.fi',
                'Referer': 'http://www.acg.fi/' + v[0],
                'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
            }
            for pg in range(1, v[1]+1):
                data = {
                    'type': 'catL' + str(k),
                    'paged': str(pg)
                }
                yield scrapy.FormRequest(url=post_url,headers=headers,formdata=data,callback=self.page,meta={'item':item})
                print('成功',k,v,pg)
    # 分析的得到的每页的响应,发现他是json数据,把他转化成python数据类型后,得到的是一个字典,内容在msg中
    # msg中内容是字符串类型,使用正则匹配获取到其中的详情页链接并发送请求
    def page(self,response):
        item = response.meta['item']
        json_obj = response.body
        msg = json.loads(json_obj)['msg']
        href_list = re.findall(r'http://www.acg.fi/[a-z]+?/\d+?.htm'.format(),msg)
        for href in href_list:
            yield scrapy.Request(url=href,callback=self.xiangqingye,meta={'item':item})
    # 使用xpath把详情页中的图片src提取并记录到item中
    # 使用xpath把分析出详情页中的页码链接,并再次发送请求
    def xiangqingye(self,response):
        item = response.meta['item']
        src = response.xpath('//div[@id="entry-content"]//img/@src').extract_first()
        if src:
            item['src'] = src.replace(' ','')
            xiangqingye_page = response.xpath('//div[@class="page-links"]/a/@href').extract()
            if xiangqingye_page:
                for page in xiangqingye_page:
                    yield scrapy.Request(url=page,callback=self.xiangqingye,meta={'item':item})
        yield item