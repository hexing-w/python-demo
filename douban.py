# -*- coding:utf-8 -*-
from lxml import etree
import requests
import MySQLdb

conn = MySQLdb.connect(host='localhost',user='root',passwd="root",db="test",charset="utf8")
db = conn.cursor()
conn.select_db('test')
def curl_page(i):
    url = 'https://movie.douban.com/top250?start={}&filter='.format(i)
    user_agent = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  ,
                            'Referer':'http://www.douban.com' }
    # 获取网页内容
    content = requests.get(url).content.decode('utf-8') 

    html = etree.HTML(content)

    item = html.xpath('//ol/li/div[@class="item"]')
    for i in item:
        url =  i.xpath('./div[@class="pic"]/a/@href')[0]
        pic_url = i.xpath('./div[@class="pic"]/a/img/@src')[0]
        title = i.xpath('./div[@class="info"]//a/span[@class="title"]/text()')
        name = title[0].encode('UTF-8','ignore').decode('UTF-8')  

        alias = title[1].lstrip('&nbsp;/&nbsp;')  if len(title)==2 else ""
        score = i.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()')[0]
        assess = i.xpath('.//div[@class="star"]/span/text()')[-1]
        quote_tag = i.xpath('.//p[@class="quote"]/span[@class="inq"]/text()')
        quote = quote_tag[0].encode('UTF-8','ignore').decode('UTF-8') if len(quote_tag) else ""
        
        # try:
        # sql = "insert into movie(url,pic_url,name,score,assess,quote) values('"+url+"','"+pic_url+"','"+name+"','"+score+"','"+assess+"','"+quote+"')"
        sql = 'insert into movie(url,pic_url,name,alias,score,assess,quote) values("%s","%s","%s","%s","%s","%s","%s")'%(url,pic_url,name,alias,score,assess,quote)
        # print sql
        db.execute(sql)
        conn.commit()
        # except:
        #     print 'fail'
        #     conn.rollback()


if __name__ == '__main__':
    for i in range(0,10):
        m = i*25
        print m
        curl_page(m)










