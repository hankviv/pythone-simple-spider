
class url:

    url = []

    def __init__(self):
        self.url = ['https://www.renrenche.com/bj/ershouche/']
        x=1
        while x<150:
            url = 'https://www.renrenche.com/bj/ershouche/p'+str(x)
            self.url.append(url)
            x= x+1
            
    def get_url(self):
        return self.url.pop()

    def has_url(self):
        if len(self.url) == 0 :
           return False
        return True

