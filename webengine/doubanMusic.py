# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2, time
from utils import HTMLParser

CATAGORY = u"豆瓣音乐"
ENCODING = "utf-8"
URL = "http://music.douban.com/top250"
SOURCE = 4
PAGE_SIZE = 5

class doubanMusic(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        
    def __del__(self):
        pass
    
    def fetchItems(self, page = 1):
        print "douban music"
    
    def fetchBang(self):
        pass
    
