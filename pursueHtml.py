from bs4 import BeautifulSoup
import re
class pursueHtml:

    def pursue_list(self,content):
        item_res = []
        soup = BeautifulSoup(content,"html.parser")
        x = soup.findAll('li', class_="span6 list-item car-item")
        for item in x :
            item_tag_a = item.find('a')
            item_id =item_tag_a['data-car-id']
            item_title = item_tag_a['title']

            item_new_price = item.find('div','new-price').text
            item_price = item.find('div', 'price').text
            item_features = item.find('span','basic').text
            item = BeautifulSoup(item.text,"html.parser")
            item_id = item_id.strip()
            item_title = item_title.strip()
            item_price = item_price.strip()
            item_new_price = item_new_price.strip()
            item_features = item_features.strip()
            item_res.append([item_id,item_title,item_price,item_new_price,item_features])
        return item_res

    def pursue_detail(self):
        return True