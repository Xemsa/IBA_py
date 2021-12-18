import sqlite3
import xml.etree.ElementTree as ET
import logging
import configparser

import os
import sys


class Database(object):

    def __init__(self,DB_LOCATION=''):
        if DB_LOCATION == '':
            self.connection=sqlite3.connect('file:cachedb?mode=memory&cache=shared')
        else:        
            self.connection = sqlite3.connect(DB_LOCATION)
        self.cur = self.connection.cursor()

    def creatab(self,name:str, list:list) -> bool:
        # print('создание таблицы',"CREATE TABLE {} ({});".format(name, ','.join(list)))
        self.cur.execute("CREATE TABLE IF NOT EXISTS {} ({});".format(name, ','.join(list)))

    def insertab(self,tab_name:str, colum:list,data:list) -> bool:
        self.__hh= ','.join(colum)
        # print('hh =',self.__hh)
        self.__bb=',?'*len(colum)
        if isinstance(data[0], list):
            for irow in data:
                # print('вставляем',"INSERT INTO {0} ({1}) VALUES ({2});".format(tab_name,self.__hh,self.__bb[1:]), irow)
                self.cur.execute("INSERT INTO {0} ({1}) VALUES ({2});".format(tab_name,self.__hh,self.__bb[1:]), irow)
        else:
            # print('вставляем',"INSERT INTO {0} ({1}) VALUES ({2});".format(tab_name,self.__hh,self.__bb[1:]), data)
            self.cur.execute("INSERT INTO {0} ({1}) VALUES ({2});".format(tab_name,self.__hh,self.__bb[1:]), data)

    def close(self):
        """close sqlite3 connection"""
        self.connection.close()

    def drop(self,tab_name:str):
        self.cur.execute("DROP TABLE {0} ;".format(tab_name))
       
    def execute(self, new_data):
        """execute a row of data to current cursor"""
        self.cur.execute(new_data)

    def commit(self):
        self.connection.commit()



if __name__ == '__main__':

    import pzz_csv
    # from pzz_lib import workname
    import pzz_config
    config = pzz_config.pzzconfig()
    Qcsv=pzz_csv.pzzcsv(config.csv)

    tab1N = config.config['DB']['Tab1']
    tab1F = config.config['DB']['Filds1'].split(",")
    if Qcsv.getheader() != tab1F:
        print('Поля в конфиге и в csv не совпадают')
        print(Qcsv.getheader())
        print(tab1F)

    tab2N = config.config['DB']['Tab2']
    tab2F = config.config['DB']['Filds2'].split(",")
    T2S = config.config['DB']['T2select']

    tab3N = config.config['DB']['Tab3']
    tab3F = config.config['DB']['Filds3'].split(",")
    T3S = config.config['DB']['T3select']

    db=Database()
    # db.drop(tab1N)
    # db.drop(tab2N)
    # db.drop(tab3N)
    # Fil= pzz_csv.pzzconfig()
    db.creatab(tab1N,tab1F)
    db.insertab(tab1N,tab1F,Qcsv.getlist())
    db.creatab(tab2N,tab2F)
    db.creatab(tab3N,tab3F)
    db.commit()


    # заполняем таблицу заказов
    # тут абстракция и потекла :,(
    # db.cur.execute("SELECT dense_rank() OVER ( ORDER BY pzztime,phone ASC) as id,\
    #     pzztime,strit,house,phone,payment, sum(price) as total \
    #     FROM csvtemp where pzztime <> 'pzztime' group by pzztime,strit,house,phone,payment;")
    db.execute(T2S)
    T2result = db.cur.fetchall()

    for i in T2result:
        # print(list(i))
        db.insertab(tab2N,tab2F,list(i))
    db.commit()

    # заполняем таблицу пиццы
    # id,pzztime,pizza,cheese,price,phone
    
    # db.cur.execute("SELECT dense_rank() OVER ( ORDER BY pzztime,phone ASC) as id, \
    #     pzztime,pizza,cheese,price,phone \
    #     FROM csvtemp where pzztime <> 'pzztime' ;")
    # db.cur.execute(T3S)
    db.execute(T3S)
    T3result = db.cur.fetchall()

    for i in T3result:
        # print(list(i))
        db.insertab(tab3N,tab3F,list(i))
    db.commit()

    db.cur.execute("SELECT * FROM {};".format(tab2N))
    one_result = db.cur.fetchall()
    for i in one_result:
        print(i)

    db.cur.execute("SELECT * FROM {};".format(tab3N))
    one_result = db.cur.fetchall()
    for i in one_result:
        print(i)
    db.close()
    print('конец')