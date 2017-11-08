from bs4 import BeautifulSoup

class pursueHtml:

    def pursue_list(self,content):
        soup = BeautifulSoup(content,"html.parser")
        x = soup.findAll('li', class_="span6 list-item car-item")
        for item in x :
            #print(item)
            #item = BeautifulSoup(item.text,"html.parser")
            item_title =item.select('h3')
            item_price = item.findAll('div', class_="price")
            item_newPrice = item.findAll('div', class_="new-price")
            item_basic = item.findAll('span', class_="basic")
            item_favoriteBox = item.findAll('div', class_="favorite-box")
            #aprint(item_title,item_price,item_newPrice,item_basic,item_favoriteBox)
            print(item_newPrice)
    def pursue_detail(self):
        return True