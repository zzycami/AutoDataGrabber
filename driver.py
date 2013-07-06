from webengine import baozoumanhua
from damingdan import LogicBang
from damingdan import LogicItem
from damingdan import LogicMingdan

engine = baozoumanhua()
logicBang = LogicBang()
logicItem = LogicItem()
logicMingdan = LogicMingdan()


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
