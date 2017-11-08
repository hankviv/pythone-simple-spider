from bs4 import BeautifulSoup

class pursueHtml:

    def pursue_list(self,content):
        soup = BeautifulSoup(content,"html.parser")
        x = soup.findAll('li', class_="span6 list-item car-item")
        for item in x :
            item_tag_a = item.find('a')
            item_image = item.find('img')
            item_id =item_tag_a['data-car-id']
            #item_src = item_image['src']
            print(item_image['src'])
            #item = BeautifulSoup(item.text,"html.parser")
            #print(item)
            # for id in item_title:
            #
            #     print(id['data-car-id'])
            #print(item.find('div','data-car-id'))
            #item_title =item.select('h3')
            #item_price = item.findAll('div', class_="price")
            #item_newPrice = item.findAll('div', class_="new-price")
            #item_basic = item.findAll('span', class_="basic")
            #item_favoriteBox = item.findAll('div', class_="favorite-box")
            #aprint(item_title,item_price,item_newPrice,item_basic,item_favoriteBox)
            #print(item_newPrice)
            # item_span = item.findAll('span')
            # print(item.h3)
            # for a in item_span:
            #     print(a)
    def pursue_detail(self):
        return True