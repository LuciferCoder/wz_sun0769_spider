# coding=utf-8

import requests
from lxml import etree

start_urls ='http://wz.sun0769.com/index.php/question/report?page=30'

r =requests.get()
print(r)
# with open("text.html",'w', encoding='utf-8') as fp:
#     fp.write(r.text.decode().encode("utf-8"))
# tree = etree.HTML(r.text)
# tr_list = tree.xpath('//div[@class="greyframe"]/table[2]/tbody/tr/td/table/tbody/tr')
# print(tr_list)
#

