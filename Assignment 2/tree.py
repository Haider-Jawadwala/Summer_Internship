import cv2
import numpy as np
from PIL import Image
img= cv2.imread(r'Original/tree.png')
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#GRAYSCALE
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale", gray)
cv2.imwrite("Manipulated/tree_GRAYSCALE.JPG",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Blur
blur = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("Blur", blur)
cv2.imwrite("Manipulated/tree_Blur.JPG",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
#canny
edge = cv2.Canny(img, 50, 150)
cv2.imshow("Canny",edge)
cv2.imwrite("Manipulated/tree_canny.JPG",edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Erode
kernel = np.ones((3, 3), np.uint8)
erode = cv2.erode(img, kernel, iterations=1)
cv2.imshow("Erode",erode)
cv2.imwrite("Manipulated/tree_Erode.JPG",erode)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Dilate
dilate = cv2.dilate(img, kernel, iterations=1)
cv2.imshow("Dilate",dilate)
cv2.imwrite("Manipulated/tree_Dilate.JPG",dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Resize Small
small = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)
cv2.imshow("Small",small)
cv2.imwrite("Manipulated/tree_Resize_Small.JPG",small)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Resize Upto Screen Size
big = cv2.resize(img, (1366,768)) 
cv2.imshow("Big",big)
cv2.imwrite("Manipulated/tree_Resize_Upto_Screen_Size.JPG",big)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Crop
crop = img[10:500, 20:400]
cv2.imshow("Crop",crop)
cv2.imwrite("Manipulated/tree_Crop.JPG",crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Rectangle
rec = cv2.rectangle(img,(20,5),(250,200),(255, 0, 0),2)
cv2.imshow("Rectangle",rec)
cv2.imwrite("Manipulated/tree_Rectangle.JPG",rec)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Circle
img= cv2.imread(r'Original/tree.png')
cir = cv2.circle(img,(140,70),100,(255, 0, 0),3)
cv2.imshow("Circle",cir)
cv2.imwrite("Manipulated/tree_Circle.JPG",cir)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Vertical Join
img= cv2.imread(r'Original/tree.png')
vert = cv2.vconcat([img, img])
cv2.imshow("Vertical",vert)
cv2.imwrite("Manipulated/tree_Vertical_Join.JPG",vert)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Horizontal Join
hor = cv2.hconcat([img, img])
cv2.imshow("Horizontal",hor)
cv2.imwrite("Manipulated/tree_Horizontal_Join.JPG",hor)
cv2.waitKey(0)
cv2.destroyAllWindows()
       
