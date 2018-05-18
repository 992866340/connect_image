# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.request
import urllib.parse
import os
import re
class ImagePipeline(object):
    # 声明计数器a
    def __init__(self):
        super().__init__()
        self.a = 0
        self.s = []
    # 把计数器当作图片名
    # 获取到的src类似 www.xxx./aaa汉字/aaa111汉字,bbb
    # 有个别src太难获取,直接except
    def process_item(self, item, spider):
        # 判断src中的汉字
        pattern = re.compile(u'[\u4e00-\u9fa5]')
        self.a += 1
        src = dict(item)['src']
        if src not in self.s:
            self.s.append(src)
            print('*'*50)
            print(src)
            needchanges = re.findall(pattern,src)
            # 将匹配到的每一个汉字都替换成其编码
            if needchanges:
                for needchange in needchanges:
                    afterchange = urllib.parse.quote(needchange)
                    src = src.replace(needchange,afterchange)
            print(src)
            print('*'*100)
            # 对src发送请求并保存到图库文件夹下
            headers = {
                'Accept': 'image/webp,image / apng, image / *, * / *;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'Host': 'img.gov.com.de',
                'Referer': 'http://www.acg.fi/anime/49332.htm',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
            }
            request = urllib.request.Request(src,headers=headers)
            response = urllib.request.urlopen(request)
            dir = r'E:\Python代码\python1710\masaike\image\image\spiders\图库'
            filepath = os.path.join(dir,'{}.jpg'.format(self.a))
            with open(filepath, 'wb') as fp:
                fp.write(response.read())
        else:
            pass
        return item