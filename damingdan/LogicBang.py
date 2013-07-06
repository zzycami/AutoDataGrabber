import sys, time
from database import database


class LogicBang(database):
    def __init__(self):
        database.__init__(self)
        self.table = "tbl_bang"

    def __del__(self):
        pass

    def addBang(self, bang):
        # check if already have this one
        bangId = self.checkBangExist(bang["title"])
        if bangId != False:
            print "bang %s already exists"%(bang["title"])
            return int(bangId)
        # create a new bang
        bangId = database.create(self, self.table, bang)

        # Synchronous bang status
        bangStatus = {}
        bangStatus["id"] = bangId
        bangStatus["items"] = 0
        bangStatus["fans"] = 0
        bangStatus["votes"] = 0
        bangStatus["update_time"] = int(time.time())
        database.create(self, "tbl_bang_stats", bangStatus)
        

    def checkBangExist(self, title):
        condition = {}
        condition["title"] = title
        return database.checkExist(self, self.table, condition)

    def incrBangStats(self, bangId, field, increment):
        condition = {}
        condition["id"] = bangId
        database.increse(self, "tbl_bang_stats", field, increment, condition)

    def decrBangStats(self, bangId, field, decrement):
        condition = {}
        condition["id"] = bangId
        database.decrese(self, "tbl_bang_stats", field, decrement, condition)
        

if __name__ == "__main__":
    logicBang = LogicBang()
    bangObj = {}
    bangObj["title"] = "testcccs"
    bangObj["description"] = "This a damingdan application interface by python"
    bangObj["class"] = 1
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
    logicBang.addBang(bangObj)
