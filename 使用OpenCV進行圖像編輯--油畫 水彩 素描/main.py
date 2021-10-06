#油畫效果
import cv2
img = cv2.imread('img.jpg')
res = cv2.xphoto.oilPainting(img, 7, 1)

#水彩效果
import cv2
img = cv2.imread('img.jpg')
res = cv2.stylization(img, sigma_s=60, sigma_r=0.6)
# sigma_s控制邻域的大小。范围1-200
# sigma_r控制邻域内不同颜色的平均方式。较大的sigma_r导致恒定颜色的较大区域。范围0-1


#黑白和彩色鉛筆素描
import cv2 
img = cv2.imread('img.jpg')
dst_gray, dst_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05) 
# sigma_s 和 sigma_r 在形式上是相同的。
# shade_factor是输出图像强度的简单缩放。值越高，结果越亮。范围0-0.1。