'''
https://www.runoob.com/sqlite/sqlite-python.html
'''

import cv2
import numpy as np
import os
from PIL import Image, ImageDraw, ImageFont
import sqlite3

conn = sqlite3.connect('user.db')
db = conn.cursor()

#使用舊版opencv-contrib-python，例如：版本3.4.3.18
recognizer = cv2.face.LBPHFaceRecognizer_create()  # 用OpenCV中LBPH算法建立人臉數據模型傳給recognizer
recognizer.read('train/train.yml')  # recognizer讀取train目錄中的train.yml檔案
cascadePath = "haarcascade_frontalface_default.xml"  #設定.xml檔案目錄
faceCascade = cv2.CascadeClassifier(cascadePath)  #導入人臉辨識工具
#sudo apt-get install fonts-noto-cjk
# font = ImageFont.truetype('NotoSerifCJK-Regular.ttc', 40)  # linux 設定字型大小

fontpath = "C:\\Windows\\Fonts\\msjhbd.ttc" # windows 設定字型
font = ImageFont.truetype(fontpath, 40) # windows設定大小

id = 0
# names = ['name1', 'name2', 'name3'] # 依 id 對應名字
camema = cv2.VideoCapture(0) # Linux 對應/dev/video0的攝影機，windows對應第一個攝影機
camema.set(3, 640) # 設定影片寬度
camema.set(4, 480) # 設定影片高度
minW = 0.1*camema.get(3)  #設定辨識影像寬
minH = 0.1*camema.get(4)  #設定辨識影像高
blue = (255,0,0)
green = (0,255,0)
red = (0,0,255)
while True:
    ret, img = camema.read()  #讀取攝影機
    img = cv2.flip(img, 1)  #img影像左右水平翻轉
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #img轉換成灰階傳給gray
    faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5, minSize = (int(minW), int(minH)) )  #辨識影像
    for(x,y,w,h) in faces:  #把人臉參數放入x,y,w,h
        cv2.rectangle(img, (x,y), (x+w,y+h), green, 2)  #在人臉用綠色繪製方框
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w]) #分析人臉相似度給confidence，編號給ID

        if (confidence < 100):  #如果相似度小於100
            cursor = db.execute("SELECT id, name FROM user WHERE id = '%s'" % id)  #用ID到user資料表查詢出name
            for row in cursor:  # 把 cursor內的資料依序放到 ROW
                name = row[1]  # row[1]->name

            # name = names[id]
            confidence = str(100 - round(confidence)) +"%"  #100-四捨五入confidence再給confidence
        else:
            name = "未知"
            confidence = str(100 - round(confidence)) +"%" 
        imgPIL = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) #cv2轉換成陣列物件
        draw = ImageDraw.Draw(imgPIL) #將陣列物件作轉換成影像
        draw.text((x+5,y-5), str(name), font=font, fill=blue)  #在影像下方用藍色字體顯示名子
        draw.text((x+5,y+h-5), str(confidence), font=font, fill=red) #在影像下方用紅色字體顯示相似度
        img = cv2.cvtColor(np.asarray(imgPIL),cv2.COLOR_RGB2BGR) #陣列物件轉換成cv2

    cv2.imshow('image',img) #顯示img在電腦上
    keyDown = cv2.waitKey(10) & 0xff #等待0.01秒判斷?鍵
    if keyDown == 27: #按下ESC按鍵，中斷while迴圈
        break

print("\n程式結束")
camema.release()  # 將攝影機設為待機狀態
cv2.destroyAllWindows()  #關閉全部視窗