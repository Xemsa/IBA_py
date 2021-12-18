import sqlite3
import xml.etree.ElementTree as ET
import logging
import configparser
import csv
import os
import sys
import pzz_config
import pzz_lib
import pzz_csv
import pzz_lite


# 1 Подтягиваем конфиг INI
config = pzz_config.pzzconfig()

tab1N = config.config['DB']['Tab1']
tab1F = config.config['DB']['Filds1'].split(",")

tab2N = config.config['DB']['Tab2']
tab2F = config.config['DB']['Filds2'].split(",")
T2S = config.config['DB']['T2select']

tab3N = config.config['DB']['Tab3']
tab3F = config.config['DB']['Filds3'].split(",")
T3S = config.config['DB']['T3select']

# 2 читаем файл CSV
Zcsv = pzz_csv.pzzcsv(config.csv)
if Zcsv.getheader() != tab1F:
    print('Поля в конфиге и в csv не совпадают')
    print('Zcsv.getheader()',Zcsv.getheader())
    print('tab1F',tab1F)

# 3 записываем в базу SQLite3
db=pzz_lite.Database()

db.creatab(tab1N,tab1F)
db.insertab(tab1N,tab1F,Zcsv.getlist())
db.commit()

db.creatab(tab2N,tab2F)
db.execute(T2S)
T2result = db.cur.fetchall()
for i in T2result:
    # print(list(i))
    db.insertab(tab2N,tab2F,list(i))
db.commit()

db.creatab(tab3N,tab3F)



# 4 нормалиуем
# 5 обрабатываем
# 6 сбрасываем в XML