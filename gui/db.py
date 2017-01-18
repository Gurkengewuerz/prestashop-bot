import pymysql
import sys
from dbsettings import connection_properties


class DB:
    conn = None

    def connect(self):
        self.conn = pymysql.connect(**connection_properties)
        return self.conn

    def query(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
        except (AttributeError, pymysql.err.OperationalError):
            print("FAILED TO SEND QUERY - RECONNECT")
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
        return cursor

    def close(self):
        self.conn.close()
