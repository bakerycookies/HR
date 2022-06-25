'''
https://www.runoob.com/sqlite/sqlite-python.html
'''
import sqlite3
#2022/06/25
conn = sqlite3.connect('user.db')  #用sqlite3去連結user.db，如果沒建立user.db會自動建立
print ("資料庫打開成功")
cursor = conn.cursor()  #連接游標
cursor.execute('''CREATE TABLE user
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL
       );''')
#執行建立一個user的資料表
#裡面放ID和name
#ID屬性 : 整數、主要的key，不可以重複、不可留空
#name屬性 : 文字、不可留空
print ("建立成功")
conn.commit() #確認
conn.close()  #關閉