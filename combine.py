import os
from damingdan import LogicBang
from damingdan import LogicItem
from damingdan import LogicMingdan
from damingdan import LogicTopic

logicBang = LogicBang()
logicItem = LogicItem()
logicMingdan = LogicMingdan()


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
                
def createBangFromWeb():
    bang = engine.fetchBang()
    print "start create bang %s"%(bang["title"])
    bangId = logicBang.addBang(bang)
    for i in range(1, 5):
        items = engine. fetchItems(i)
        for item in items:
            print "create item %s"%(item["title"])
            comment = {}
            itemId = logicItem.addItem(item, comment)
            logicMingdan.nominate(bangId, itemId)   

if __name__ == '__main__':
    engines = getEngines()
    for engineStr in engines:
        INSTANCE_STR = "engine =  %s.%s()"%(engineStr, engineStr)
        exec INSTANCE_STR
        engine.fetchItems(1)
    
    