from PIL import Image
import pytesseract as ocr 
import cv2 
import numpy as np 


###########二元化
def binarizing(img,threshold):
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img

###########去除干擾線
def depoint(img):   #input: gray image
    pixdata = img.load()
    w,h = img.size
    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            if pixdata[x,y-1] > 245:
                count = count + 1
            if pixdata[x,y+1] > 245:
                count = count + 1
            if pixdata[x-1,y] > 245:
                count = count + 1
            if pixdata[x+1,y] > 245:
                count = count + 1
            if count > 2:
                pixdata[x,y] = 255
    return img

########識別全部
def all_OCR(img1):
    ##圖片放大3倍
    out=img1.resize((w*3,h*3),Image.ANTIALIAS)
    # 轉成灰階圖
    img= out.convert('L')
    # 轉成binary圖片
    img1=binarizing(img,100)
    img2=depoint(img1)
    # img2.show()
    code = ocr.image_to_string(img2,lang="chi_tra")
    return code.split('\n')


