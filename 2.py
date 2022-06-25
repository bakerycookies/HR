import cv2
import numpy as np
from PIL import Image
import os
path = 'images'  #設定影像檔存放目錄
recognizer = cv2.face.LBPHFaceRecognizer_create() #初始化人臉檢測器和人臉識別器
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml"); #導入辨識工具

def getFaceAndID(path):
    images = [os.path.join(path,f) for f in os.listdir(path)]  #把path檔案名稱放入F，再把F放入images串列中   
    FaceList = []  
    IDList = []
    for image in images:  #把images資料依序放入image
        img = Image.open(image).convert('L')  #轉換成灰階放入img
        img_np = np.array(img,'uint8')  #把img傳入np設定8X8的串列放入img_np
        id = int(os.path.split(image)[-1].split(".")[1])  #抓取image資料夾中的圖像檔檔名
        faces = detector.detectMultiScale(img_np)  #找出img_np圖片中的人臉
        for (x,y,w,h) in faces:  #把人臉參數放入x,y,w,h
            FaceList.append(img_np[y:y+h,x:x+w])  #img_np串列資料加入FaceList串列
            IDList.append(id)  #id加入IDList串列
    return FaceList, IDList  #回傳face,ID的值

print ("\n影像辨識中")
face, id = getFaceAndID(path) #呼叫上面副函數把path值傳入，取得face,ID的值
recognizer.train(face, np.array(id))  #依face和id訓練人臉資料
recognizer.write('train/train.yml') #儲存訓練結果到train目錄中的train.yml檔案
print("\n訓練出{0}張臉".format(len(np.unique(id))))