import sys, time
from database import database

class LogicItem(database):
    def __init__(self):
        database.__init__(self)
        self.table = "tbl_item"

    def __del__(self):
        pass

    # need add the comment image path
    def addItem(self, item, comment):
        # check repeat
        if self.checkItemExist(item["title"]):
            print "item %s already exist"%(item["title"])
            return False
        
        itemId = database.create(self, self.table, item)

        # set the damingdan admin to be the owner
        self.addItemOwner(itemId, 1, 1)

        comment = {}
        comment["mingdan_id"] = -1
        comment["item_id"] = itemId
        comment["content"] = item["title"]
        comment["user_id"] = 1
        comment["dings"] = 0
        comment["cais"] = 0
        comment["create_time"] = int(time.time())
        comment["status"] = 0
        comment["img_src"] = item["image"]
        database.create(self, "tbl_comment", comment)

        return itemId

        
    def checkItemExist(self, title):
        condition = {}
        condition["title"] = title
        return database.checkExist(self, self.table, condition)

    def addItemOwner(self, itemId, userId, status = 0):
        itemOwner = {}
        itemOwner["item_id"] = itemId
        itemOwner["user_id"] = userId
        itemOwner["status"] = status
        return database.create(self, self.table, itemOwner)

    def incrItemStats(self, itemId, field, increment):
        condition = {}
        condition["id"] = itemId
        database.increse(self, self.table, field, increment, condition)

    def decrItemStats(self, itemId, field, decrement):
        condition = {}
        condition["id"] = itemId
        database.decrese(self, self.table, field, decrement, condition)



if __name__ == "__main__":
    logicItem = LogicItem()
    item = {}
    item["title"] = "cs";
    logicItem.addItem(item, item)
