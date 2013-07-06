# -*- coding: cp936 -*-
from bs4 import BeautifulSoup
import urllib2, time
from utils import HTMLParser


CATAGORY = "暴走漫画"
ENCODING = "utf-8"
URL = "http://baozoumanhua.com/groups/1/hottest/week/page/"
SOURCE = 4
PAGE_SIZE = 5

    
class baozoumanhua(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        

    def __del__(self):
        pass

    def fetchItems(self, page = 1):
        self.html = HTMLParser.fetchPage(self, "%s%d"%(URL, page))
        self.soup = BeautifulSoup(self.html, from_encoding=ENCODING)
        
        entryList = self.soup.find("ul", id="entry-list-ul")
        items = []
        for entry in entryList.find_all("li"):
            item = {}
            item["foreign_id"] = entry.get("data-id")
            item["title"] =  entry.get("data-text")
            item["source"] = SOURCE
            item["url"] = entry.get("data-url")
            item["image"] = entry.find("img")["src"]
            item["creator"] = 1
            item["create_time"] = int(time.time())
            item["fans"] = 0
            item["bangs"] = 1
            item["is_verified"] = 1
            item["verified_word"] = u"暴走漫画站点刊登的漫画"
            item["status"] = 0
            items.append(item)
        return items

    def fetchBang(self):
        bangObj = {}
        now = time.localtime(time.time())
        bangObj["title"] = u"暴走漫画一周最热排行榜-%d-%d-%d"%(now.tm_year, now.tm_mon, now.tm_mday)
        bangObj["description"] = u"暴走漫画一周最热排行榜-%d-%d-%d"%(now.tm_year, now.tm_mon, now.tm_mday)
        # use damingdan admin account
        bangObj["sponsor"] = 1
        bangObj["create_time"] = int(time.time())
        bangObj["vote_start"] = bangObj["create_time"]
        bangObj["vote_end"] = 0
        bangObj["is_slided"] = 1
        bangObj["slide_window"] = 7
        bangObj["is_lbs"] = 0
        bangObj["jingdu"] = 0.00
        bangObj["weidu"] = 0.00
        bangObj["poi_name"] = ""
        bangObj["lbs_radix"] = 0
        bangObj["nominate_level"] = 0
        bangObj["vote_level"] = 0
        bangObj["status"] = 0
        return bangObj

