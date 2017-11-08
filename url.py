
class url:

    url = []

    def __init__(self):
        self.url = ['https://www.renrenche.com/sh/ershouche/']
        x=1
        while x<300:
            url = 'https://www.renrenche.com/sh/ershouche/p'+str(x)
            self.url.append(url)
            x= x+1
            
    def get_url(self):
        return self.url.pop()

    def has_url(self):
        if len(self.url) == 0 :
           return False
        return True

