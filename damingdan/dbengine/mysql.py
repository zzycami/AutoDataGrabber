import MySQLdb, types

def implode(arr):
    return ','.join(arr)
    

class mysql:
    def __init__(self, host, user, password, db, port):
        try:
            self.connect = MySQLdb.connect(host=host,user=user,passwd=password,db=db,charset="utf8")
            #self.connect.select_db(db)
            self.cursor = self.connect.cursor()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s"%(e.args[0], e.args[1])
            
    def __del__( self ):
        self.cursor.close()
        self.connect.close()

    def query(self, sql):
        try:
            self.cursor.execute(sql)
            return self.cursor.lastrowid
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s"%(e.args[0], e.args[1])

    def create(self, table, obj):
        try:
            keys = [];
            values = []
            for key, value in obj.items():
                keys.append(key)
                if isinstance(value, str) or isinstance(value, unicode):
                    values.append("\'%s\'"%(value))
                else:
                    values.append(str(value))

            keyStr = implode(keys)
            valueStr = implode(values)
            sql = "insert into %s(%s) values(%s)"%(table, keyStr, valueStr)
            #print sql
            return self.query(sql);
                
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s"%(e.args[0], e.args[1])

    def setCondition(self, condition):
        if(isinstance(condition, dict)):
            keys = [];
            values = []
            conditions = ""
            first = True
            for key, value in condition.items():
                keys.append(key)
                if isinstance(value, str) or isinstance(value, unicode):
                    value = "\'%s\'"%(value)
                if first:
                    conditions += "%s=%s "%(key, value)
                    first = False
                else:
                    conditions += "and %s=%s "%(key, value)
            return conditions
        else:
            return condition
                

    def delete(self, table, condition):
        try:
            condition = self.setCondition(condition)
            if condition != None:
                sql = "delete from %s where %s"%(table, condition)
                
            #print sql
            return self.query(sql);
                
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s"%(e.args[0], e.args[1])

    def update(self, table, obj, condition):
        try:
            updateField = ""
            first = True
            for key, value in obj.items():
                if isinstance(value, str) or isinstance(value, unicode):
                    value = "\'%s\'"%(value)
                if first:
                    updateField += "%s=%s"%(key, value)
                    first = False
                else:
                    updateField += ", %s=%s"%(key, value)
                    
            condition = self.setCondition(condition)
            
            if condition != None:
                sql = "update %s set %s where %s"%(table, updateField, condition)
                
            #print sql
            return self.query(sql);
                
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s"%(e.args[0], e.args[1])

    def increse(self, table, field, incremental, condition):
        try:
            condition = self.setCondition(condition)
            sql = "update %s set %s = %s + %s where %s"%(table, field, field, incremental, condition)
            #print sql
            return self.query(sql);
                
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s"%(e.args[0], e.args[1])

    def decrese(self, table, field, decremental, condition):
        try:
            condition = self.setCondition(condition)
            sql = "update %s set %s = %s - %s where %s"%(table, field, field, decremental, condition)
            return self.query(sql);
                
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s"%(e.args[0], e.args[1])

    def fetchOne(self, table, fields, condition):
        try:
            condition = self.setCondition(condition)
            if fields != None and condition != None:
                sql = "select %s from %s where %s"%(fields, table, condition)
                num = self.cursor.execute(sql)
                return self.cursor.fetchone()
            else:
                return False
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s"%(e.args[0], e.args[1])

    def fetchAll(self, table, fields, condition):
        try:
            condition = self.setCondition(condition)
            if fields != None and condition != None:
                sql = "select %s from %s where %s"%(fields, table, condition)
                num = self.cursor.execute(sql)
                return self.cursor.fetchall()
            else:
                return False
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s"%(e.args[0], e.args[1])

    def checkExist(self, table, condition):
        res = self.fetchOne(table, "count(id) as num", condition)
        num = res[0]
        if num > 0:
            return True
        else:
            return False


        
if __name__ == "__main__":
    db = mysql(host="127.0.0.1", user="root", password="", db="db_damingdan", port="3306")
    #db.query("insert into tbl_poi(name, jingdu, weidu, address, type) values ('zhouzeyong', 12.6, 34.7, 'zhouzeong', 'dskhdk')")
    poi = {}
    condition = {}
    poi["weidu"] = 6382919
    poi["type"] = "hehehehehehrsehe"
    condition["id"] = 7
    print db.update("tbl_poi", poi, condition)
    
