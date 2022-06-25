'''
https://github.com/opencv/opencv/tree/master/data/haarcascades

https://www.jianshu.com/p/881d7194267d
sudo apt-get update
sudo apt-get install cmake
sudo apt-get install build-essential libgtk2.0-dev libavcodec-dev libavformat-dev libjpeg-dev libswscale-dev libtiff5-dev
sudo apt-get install libgtk2.0-dev
sudo apt-get install pkg-config
sudo apt-get update

https://sites.google.com/site/zsgititit/home/raspberry-shu-mei-pai/raspberry3shi-yongwebcam-opencv-jin-xing-ren-lian-bian-shi

https://tw511.com/a/01/28496.html

pip3 list | findstr opencv

pip3 install opencv-python==4.5.2.52
pip3 install opencv-contrib-python==4.5.2.52
pip3 install Pillow==9.0.1
pip3 install --upgrade numpy
sudo apt-get update
sudo apt-get install libhdf5-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
sudo apt-get install libqt4-test
sudo apt-get install libqtgui4
sudo apt-get update

# pip install opencv-python-headless==4.5.2.52
# pip uninstall opencv-python-headless==3.4.3.18

要先 images/str(id)資料夾

https://blog.csdn.net/qq_38269799/article/details/83384291

'''
import cv2

camema = cv2.VideoCapture(0)  # Linux 對應/dev/video0的攝影機，windows對應第一個攝影機
camema.set(3, 640) # 設定影片寬度
camema.set(4, 480) # 設定影片高度
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # 導入辨識工具
id = input('\n請輸入id？') 
print("\n 初始化錄影機，請等待")
count = 0 # 計算存幾張人臉
while(True):
    ret, img = camema.read()
    img = cv2.flip(img, 1) #設定影像左右互換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #轉換成灰階
    faces = detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)  #辨識影像
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #加上綠框
        count += 1
        cv2.imwrite("images/User." + str(id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])  #儲存影像到IMAGES資料夾
        cv2.imshow('image', img)
        print('儲存第 '+str(count)+ ' 個人臉')
    keyDown = cv2.waitKey(100) & 0xff #等待0.1秒，偵測鍵盤按鍵是否按下
    if keyDown == 27: #按下ESC按鍵，中斷while迴圈
        break
    elif count >= 100: # 儲存100張人臉後，中斷while迴圈
        break
print("\n 偵測完成")
camema.release() # 將攝影機設為待機狀態
cv2.destroyAllWindows() # 關閉全部視窗