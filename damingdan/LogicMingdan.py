# -*- coding: utf-8 -*-
import sys, time
from database import database
from LogicBang import LogicBang
from LogicItem import LogicItem


class LogicMingdan(database):
    def __init__(self):
        database.__init__(self)
        self.table = "tbl_mingdan"

    def __del__(self):
        pass

    def nominate(self, bangId, itemId):
        # check if already nominate
        if self.checkNominate(bangId, itemId):
            print "Already nominate bang id:%d, item id:%s"%(bangId, itemId)
            return False
        mingdan = {}
        mingdan["bang_id"] = bangId
        mingdan["item_id"] = itemId
        mingdan["user_id"] = 1
        mingdan["list_time"] = int(time.time())
        database.create(self, self.table, mingdan)
        
        # update the statitcs
        logicBang = LogicBang()
        logicBang.incrBangStats(bangId, "items", 1)
        logicItem = LogicItem()
        logicItem.incrItemStats(itemId, "bangs", 1)
        condition = {}
        condition["id"] = bangId
        bangStatus = {}
        bangStatus["update_time"] = int(time.time())
        database.update(self, "tbl_bang_stats", bangStatus, condition)
        
        

    def checkNominate(self, bangId, itemId):
        condition = {}
        condition["bang_id"] = bangId
        condition["item_id"] = itemId
        return database.checkExist(self, self.table, condition)

if __name__ == "__main__":
    logicMingdan = LogicMingdan()
    logicMingdan.nominate(9, 3)
