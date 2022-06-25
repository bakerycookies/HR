'''
https://yanwei-liu.medium.com/python%E8%B3%87%E6%96%99%E5%BA%AB%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-%E5%85%AD-sqlite3-818ca8e7eff5
'''
import sqlite3

conn = sqlite3.connect('user.db')  #用sqlite3去連結user.db
cursor = conn.cursor()  #連接游標
print ("資料庫打開成功")

cursor.execute("INSERT INTO user (ID, NAME) \
      VALUES (0, '徐忠凱')")  #在user資料表插入ID,NAME 值為(0,Apple)

cursor.execute("INSERT INTO user (ID, NAME) \
      VALUES (1, '徐秉辰')")   #在user資料表插入ID,NAME 值為(1,徐秉辰)

conn.commit()  #確認
print ("數據插入成功")
conn.close()  #關閉