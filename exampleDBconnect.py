import requests
import selectorlib
import time
import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("database\\data2.db")

    def Create(self,table):
        # insert _rows
        cursor = self.connection.cursor()
        new_rows = [("New", "New", "2000-10-10")]
        cursor.executemany(" insert into emp values(?,?,?)", new_rows)
        self.connection.commit()
        print(f"i'm in create")
        DB.Read(table)

    def Read(self,table):
        cursor = self.connection.cursor()
        cursor.execute(f"Select * from '{table}'")
        rows = cursor.fetchall()
        print(f"i'm in read {rows}")


    def Update(self,table,setValue,cond):
        cursor = self.connection.cursor()
        uprows = [(table, setValue, cond)]
        stmt=f" update {table} set first_name='{setValue}' where first_name='{cond}'"
        print(stmt)
        cursor.execute(stmt)
        self.connection.commit()
        print("i'm in UPDATE")
        DB.Read(table)


    def Delete(self, table, value):
        cursor = self.connection.cursor()
        stmt=f" Delete from {table} where last_name='{value}'"
        cursor.execute(stmt)
        self.connection.commit()
        print("i'm in Delete")
        DB.Read(table)

    def Close(self):
        self.connection.close()
        print("DB connection closed")



if __name__ =="__main__":
    DB=Database()
    DB.Read("emp")
    #DB.Create("emp")
   # DB.Update("emp","Old","New")
    #DB.Delete("emp","New")
    DB.Close()
# connection=sqlite3.connect("database\\data2.db")
# cursor=connection.cursor()
#
# cursor.execute("Select * from emp")
# rows=cursor.fetchall()
# print(rows)
# #insert _rows
# new_rows=[("New","New","1999-10-10")]
# cursor.executemany(" insert into emp values(?,?,?)",new_rows)
# connection.commit()
# cursor.execute("Select * from emp")
# new=cursor.fetchall()
# print(new)
#self.connection.close()