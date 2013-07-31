from sgmllib import SGMLParser

class URLLister(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.urls=[]

    def start_a(self,attrs):
        href = [v for k, v in attrs if k =="href"]
        if href:
            self.urls.extend(href)

    def start_div(self,attrs):
        id = [v for k,v in attrs if k == "id"]
        if id:
            self.urls.extend(href)
