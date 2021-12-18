import sqlite3
import xml.etree.ElementTree as ET
import logging
import configparser
import csv
import os
import sys
import pzz_config
from pzz_lib import workname


def creatab(name:str, list:list) -> bool:
        try:
            cur.execute("CREATE TABLE {} ({});".format(name, list))
        except:
            return False
        finally:
            return True






# csv
'''


mycsv = workname(config["New_File"]['Name'])#получаем адрес файла с заказами
with open(mycsv, newline='',encoding='UTF8') as csvfile:
    # spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    spamreader = csv.DictReader (csvfile, delimiter=',', quotechar='|')
     to_db = [(i['col1'], i['col2']) for i in dr]
    for row in spamreader:
        print(row['pzztime'])
        # print(', '.join(row))
        # print(row)
'''



 # SQL 
class DB:
    def __init__(self,name):
        self.mydb = name
        self.con = sqlite3.connect(self.mydb) 
        self.cur = self.con.cursor()

    def creatab(self,name:str, list:list) -> bool:
        try:
            self.cur.execute("CREATE TABLE {} ({});".format(name, list))
        except:
            return False
        finally:
            return True


       
        


# cur.execute("INSERT INTO t VALUES(?, ? );", ['aa','bb'])
# con.commit()
def start_csv(name):
    mycsv = workname(config["New_File"]['Name'])#получаем адрес файла с заказами
    with open(mycsv, newline='',encoding='UTF8') as csvfile:
        # spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        spamreader = csv.DictReader (csvfile, delimiter=',', quotechar='|')
        to_db = [(i['col1'], i['col2']) for i in spamreader]
        for row in spamreader:
            print(row['pzztime'])
            # print(', '.join(row))
            # print(row)


# 1

# старт
config = pzz_config.pzzconfig()
mydb = config.DB
# con = sqlite3.connect(mydb)
con = sqlite3.connect('file:cachedb?mode=memory&cache=shared') #база в оперативке
cur = con.cursor()
# завели базу теперь создаём таблицу и записываем в неё csv

# 2

creatab('csvtemp',config.config["New_File"]['Filds'])


mycsv = config.csv
# workname(config["New_File"]['Name'])#получаем адрес файла с заказами
with open(mycsv, newline='',encoding='UTF8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    fields = next(spamreader)
    print('fields',fields)
    # spamreader = csv.DictReader (csvfile, delimiter=',', quotechar='|')
    # to_db = [(i['col1'], i['col2']) for i in spamreader]
    for row in spamreader:
        cur.execute("INSERT INTO csvtemp VALUES (?,?,?,?,?,?,?,?,?);", row)
        #print(row['pzztime'])
        # print(', '.join(row))
        # print(row)




# 9
cur.execute("SELECT * FROM csvtemp where pzztime <> 'pzztime';")
one_result = cur.fetchall()
print(one_result)

