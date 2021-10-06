
# Author:Color Space
# 来源-公众号：OpenCV与AI深度学习
# --------------------------------
import numpy as np
import cv2
import easyocr

reader = easyocr.Reader(['en'])
img = cv2.imread('2.png')
cv2.imshow('src', img)

B,G,R=cv2.split(img)

ret,thres= cv2.threshold(B, 230, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('thres', thres)


k1=np.ones((11,11), np.uint8)
k2=np.ones((9,9), np.uint8)
thres = cv2.morphologyEx(thres, cv2.MORPH_DILATE, k1)
thres = cv2.morphologyEx(thres, cv2.MORPH_ERODE, k2)
cv2.imshow('morph', thres)
#cv2.imwrite('morph.jpg', thres)

contours,hierarchy = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
rects = []
for cnt in contours:
  (x, y, w, h) = cv2.boundingRect(cnt)
  if w>200 or h > 200:
    #cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
    cv2.drawContours(thres,cnt,-1,(0,0,0),-1)
  if w > 10 and w < 70 or h > 50 and h < 90:
    cv2.drawContours(img,cnt,-1,(255,0,0),2)
#cv2.imwrite('morph.jpg', thres)

result = reader.readtext(thres)
if len(result) > 0:
  for i in range(0,len(result)):
    pt1 = (tuple(result[i][0][0]))
    pt2 = (tuple(result[i][0][1]))
    pt3 = (tuple(result[i][0][2]))
    pt4 = (tuple(result[i][0][3]))
    cv2.line(img,pt1,pt2,(0,0,255),2,cv2.LINE_AA)
    cv2.line(img,pt2,pt3,(0,0,255),2,cv2.LINE_AA)
    cv2.line(img,pt3,pt4,(0,0,255),2,cv2.LINE_AA)
    cv2.line(img,pt4,pt1,(0,0,255),2,cv2.LINE_AA)
    print(result[i][1])
    strText = result[i][1].replace(' ','')
    cv2.putText(img,strText,(pt1[0]+2,pt1[1]-5),0,1.0,(255,0,255),2)

else:
  print('have not found any text!')

cv2.imshow('result', img)
cv2.imwrite('result.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
print ('finish')