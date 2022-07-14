# Computer Vision 電腦視覺
import cv2

# 人臉特徵檔
face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_default.xml')

# 讀檔
frame = cv2.imread('./image/test.jpg')

# 偵測臉部，會得到臉部區域的左上角座標與長寬 (x, y, w, h)
faces = face_cascade.detectMultiScale(
    frame,  # 待檢測圖片
    scaleFactor=1.1,  # 檢測粒度
    minNeighbors=5,   # 檢測次數
    minSize=(30, 30),  # 搜尋尺寸
    flags=cv2.CASCADE_SCALE_IMAGE
)
print('臉部座標(x, y, w, h',  faces)

# 在臉部周圍畫上矩形
for (x, y, w, h) in faces:
    # 參數說明: frame, 左上角座標, 右下角座標, BGR 色碼, 框線的寬度
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

# 將影像顯示出來
cv2.imshow('My window', frame)

# 按下任意鍵離開程式
c = cv2.waitKey(0)
print(c)
