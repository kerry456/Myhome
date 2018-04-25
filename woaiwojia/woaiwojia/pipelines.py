# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

from woaiwojia.items import WoaiwojiaItem


class WoaiwojiaPipeline(object):
    def open_spider(self,spider):
        try:
            self.con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='my_home',use_unicode = True,charset='utf8')
            self.cursor = self.con.cursor()
            print('数据库链接成功……')
        except Exception as e:
            print('数据库链接失败。。')

    def process_item(self, item, spider):
        try:
            if isinstance(item,WoaiwojiaItem):
                insert_sql = '''INSERT INTO rent_info(TITLE, AREA, PRICE, RENT_METHOD, ADDRESS, URL) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')'''.format(item['title'], item['area'], item['price'], item['rent_method'], item['address'], item['url'])
            else:
                insert_sql = '''INSERT INTO rent_details VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') ''' % (
                item['title'], item['rent'], item['floor'], item['house_type'], item['area'], item['payment_method'],
                item['build_year'], item['rent_method'], item['subway'], item['contact'], item['telephone_number'])
            self.cursor.execute(insert_sql)  # 执行sql语句
            self.con.commit()  # 提交到数据库，insert和updata语句必须执行这句
            print('数据插入成功……')
        except Exception as e:
            print(e)
        return item
        # with open('1.text','a',encoding='utf-8') as f:
        #     f.write(item.get('title', ''))
        #     f.write('  |  ')
        #     f.write(item.get('area', ''))
        #     f.write('  |  ')
        #     f.write(item.get('price', ''))
        #     f.write('  |  ')
        #     f.write(item.get('rent_method', ''))
        #     f.write('  |  ')
        #     f.write(item.get('address', ''))
        #     f.write('  |  ')
        #     f.write(item.get('url', ''))
        #     f.write('  |  ')
        #     f.write('\n')
        # return item

    def close_spider(self, spider):
        self.con.close()


