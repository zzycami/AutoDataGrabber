# -*- coding: utf-8 -*-
import os, webImage
from damingdan import LogicBang
from damingdan import LogicItem
from damingdan import LogicMingdan
from damingdan import LogicTopic

logicBang = LogicBang()
logicItem = LogicItem()
logicMingdan = LogicMingdan()
logicTopic = LogicTopic()


def getEngines():
    engines = []
    # get the root of current file
    path = "%s/webengine/"%(os.path.split(__file__)[0])
    moduleList = os.listdir(path)
    for module in moduleList:
        if os.path.isfile(path + module):
            fileName, extension = os.path.splitext(module)
            if fileName != "__init__" and extension == ".py":
                engines.append(fileName)
    return engines

engines = getEngines()
for engineStr in engines:
    IMPORT_STR = "from webengine import %s"%(engineStr)
    exec IMPORT_STR
    

def addslashes(s):
    d = {'"':'\\"', "'":"\\'", "\0":"\\\0", "\\":"\\\\"}
    return ''.join(d.get(c, c) for c in s)


def createBangFromWeb(engine):
    bang = engine.fetchBang()
    if bang != None:
        print "start create bang %s"%(bang["title"])
        bangId = logicBang.addBang(bang)
        print "start add topic to the bang %s"%(bang["title"])
        topics = []
        topics.append(engine.CATAGORY)
        logicTopic.addBangTopicArray(bangId, topics)
    else:
        return False
    
    for i in range(1, engine.PAGE_SIZE):
        items = engine.fetchItems(i)
        if items == None:
            continue
        for item in items:
            if item["title"] == "" or item["title"] == None:
                continue
            print u"create item %s"%(item["title"])
            comment = {}
            itemId = logicItem.addItem(item)
            if logicMingdan.nominate(bangId, itemId) != False:
                # add a news
                newsContent = u"<a href='http://user.damingdan.com/myitems.php?u=1'>大名单</a>创建了<a href='http://www.damingdan.com/i.php?id=%d'>%s藤吧</a>"%(itemId, item["title"]);
                logicItem.addItemNews(itemId, addslashes(newsContent))

def run():
    engines = getEngines()
    for engineStr in engines:
        INSTANCE_STR = "engine =  %s.%s()"%(engineStr, engineStr)
        exec INSTANCE_STR
        createBangFromWeb(engine)

if __name__ == '__main__':
    run()
    
    