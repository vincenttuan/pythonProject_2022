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
