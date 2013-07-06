import urllib2, time

class HTMLParser:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def fetchPage(self, url):
        print "start load page: %s"%(url)
        try:
            response = urllib2.urlopen(url, None, 12)
            page = response.read()
            return page
        except:
            print "urlopen exception:" + url
            return False
    
    def fetchItems(self, page = 1):
        pass
    
    def fetchBang(self):
        pass
    
    

if __name__ == "__main__":
    parser = HTMLParser()
    parser.fetchPage("http://baozoumanhua.com/groups/1/hottest/day/page/2");
