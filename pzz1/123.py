import sqlite3


con = sqlite3.connect('file:cachedb?mode=memory&cache=shared') #база в оперативке
cur = con.cursor()

def creatab(name:str, list:list) -> bool:
        try:
            print('создание таблицы',"CREATE TABLE {} ({});".format(name, str(list)))
            cur.execute("CREATE TABLE {} ({});".format(name, str(list)))
        except:
            return False
        finally:
            return True

fild=['pzztime','estimate','pizza','cheese','price','payment','strit','house','phone']
# fild = ['f1','f2']
filds =','.join(fild)
cur.execute("DROP TABLE tab1 ;")
if creatab('tab1',filds):
    print('создали')
else:
    print('no')

cur.execute("SELECT * FROM tab1 ;")
one_result = cur.fetchall()
print('запрос из таблицы',one_result)



bb=',?'*len(fild)
val = ['2021-12-11T26:26:26','30','pepperoni','50','15','cash','Азгура','4','+375172971699']
# val = [5,2]
# print("INSERT INTO tab1 VALUES ({});".format(bb[1:]), val)
cur.execute("INSERT INTO tab1 ({}) VALUES ({});".format(filds,bb[1:]), val)
# cur.execute("INSERT INTO tab1 (f1,f2) VALUES (?,?);", val)
con.commit()


cur.execute("SELECT * FROM tab1 where price = '15';")
one_result = cur.fetchall()
print(one_result)
con.close()