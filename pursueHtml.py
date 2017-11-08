from bs4 import BeautifulSoup

class pursueHtml:

    def pursue_list(self,content):
        soup = BeautifulSoup(content,"html.parser")
        x = soup.find('li', class_="span6 list-item car-item")

      
        print(x)
    def pursue_detail(self):
        return True