import sqlite3
import xml.etree.ElementTree as ET
import logging
import configparser
import csv
import os
import sys

def workname(filename:str) -> str:
    dirname = os.path.dirname(__file__)
    wname = os.path.join(dirname, filename)
    return wname

# подключаем конфиг.ini
configname = workname('pzz_config.ini')
config = configparser.ConfigParser()  # создаём объекта парсера
config.read(configname)  # читаем конфиг

"""
Что я хочу?
xml файл с двумя(тремя) уровнями вложенности
типа
id
aa
bb
c
c1
c2
c3
c
"""
"""
logging.basicConfig()

tree = 1
print(config.sections())
for key in config["New_File"]:  
    print(key)

"""
'''
config = configparser.ConfigParser()  # создаём объекта парсера
config.read('pzz_config.ini')  # читаем конфиг

mycsv = config["New_File"]['fullpath'] #получаем адрес файла с заказами
print(mycsv)
with open(r''+str(mycsv), newline='',encoding='UTF8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
'''

# csv
mycsv = workname(config["New_File"]['Name'])#получаем адрес файла с заказами
with open(mycsv, newline='',encoding='UTF8') as csvfile:
    # spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    spamreader = csv.DictReader (csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(row['pzztime'])
        # print(', '.join(row))
        # print(row)

# SQL
con = sqlite3.connect(":memory:") # change to 'sqlite:///your_filename.db'
cur = con.cursor()
cur.execute("CREATE TABLE t (col1, col2);") # use your column names here