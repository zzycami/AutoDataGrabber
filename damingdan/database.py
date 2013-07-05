import config
EXEC_STR = "from dbengine import %s"%(config.DB_ENGINE)
exec EXEC_STR


class database:
    def __init__(self):
        host = config.DB_HOST
        user = config.DB_USER
        password = config.DB_PASSWORD
        name = config.DB_NAME
        port = config.DB_PORT
        
        EXEC_STR = "self.db = %s(host, user, password, name, port)"%(config.DB_ENGINE)
        exec EXEC_STR
        

    def query(self, sql):
        return self.db.query(sql)

    def create(self, table, obj):
        return self.db.create(table, obj)

    def delete(self, table, condition):
        return self.db.delete(table, condition)

    def update(self, table, obj, condition):
        return self.db.update(table, obj, condition)

    def fetchOne(self, table, fields, condition):
        return self.db.fetchOne(table, fields, condition)

    def fetchAll(self, table, fields, condition):
        return self.db.fetchAll(table, fields, condition)

    def checkExist(self, table, condition):
        return self.db.checkExist(table, condition)

    def increse(self, table, field, incremental, condition):
        return self.db.increse(table, field, incremental, condition)

    def decrese(self, table, field, decremental, condition):
        return self.db.decrese(table, field, decremental, condition)


if __name__ == "__main__":
    db = database()
