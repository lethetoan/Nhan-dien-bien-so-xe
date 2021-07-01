import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('bien-so-o-to-mercedes-1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 30, 200)
cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts,key = cv2.contourArea, reverse = True)
screanCnt = None
for c in cnts:
    peri = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c, 0.05 * peri, True) 
    if len(approx) == 4:
        screanCnt = approx
        x,y,w,h = cv2.boundingRect(c)
        new_img = img[y:y +h,x : x + w]
        break
cv2.drawContours(img,[screanCnt],-1,(0,255,0),2) 
cv2.imshow('ANH',img)
cv2.waitKey(0)
cv2.imshow('a',new_img)  
cv2.waitKey(0)
cv2.destroyAllWindows()  
text=pytesseract.image_to_string(new_img,lang='eng') # đọc biển số
print("Number is:" ,text)

