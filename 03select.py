import sqlite3

conn = sqlite3.connect('user.db')  #用sqlite3去連結user.db
cursor = conn.cursor()  #連接游標

id = '2' # 設定查詢的 id 值
# 用 ID 的值到 user 資料庫查詢出 id 和 name 放到 DATA
data = cursor.execute("SELECT id, name FROM user WHERE id = '%s'" % id)  #執行從user選擇ID,NAME

for row in data: # 把 DATA內的資料依序放到 ROW
   print(str(row[0])+ " " + row[1]) # 列出 row[0]->id 和 row[1]->name

conn.close()