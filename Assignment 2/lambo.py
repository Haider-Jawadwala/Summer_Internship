import cv2
import numpy as np
import pytesseract
from PIL import Image
img= cv2.imread(r'Original/lambo.png')
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#GRAYSCALE
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Manipulated/Image3/gray.JPG",gray)
#Blur
blur = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("Blur", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Manipulated/Image3/blur.JPG",blur)
#canny
edge = cv2.Canny(img, 50, 150)
cv2.imshow("Canny",edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Manipulated/Image3/canny.JPG",edge)
#Erode
kernel = np.ones((3, 3), np.uint8)
erode = cv2.erode(img, kernel, iterations=1)
cv2.imshow("Erode",erode)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Manipulated/Image3/erode.JPG",erode)
#Dialate
dilate = cv2.dilate(img, kernel, iterations=1)
cv2.imshow("Dilate",dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Manipulated/Image3/dilate.JPG",dilate)
#Resize Small
small = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)
cv2.imshow("Small",small)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Manipulated/Image3/small.JPG",small)
#Resize Upto Screen Size
big = cv2.resize(img, (1366,768)) 
cv2.imshow("Big",big)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Manipulated/Image3/big.JPG",big)
#Crop
crop = img[20:400, 75:500]
cv2.imshow("Crop",crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Manipulated/Image3/crop.JPG",crop)
#Rectangle
rec = cv2.rectangle(img,(75,20),(500,400),(255, 0, 0),2)
cv2.imshow("Rectangle",rec)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Manipulated/Image3/rectangle.JPG",rec)
#Circle
img= cv2.imread(r'Original/lambo.png')
cir = cv2.circle(img,(250,210),250,(255, 0, 0),3)
cv2.imshow("Circle",cir)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Manipulated/Image3/circle.JPG",cir)
#Vertical Join
img= cv2.imread(r'Original/lambo.png')
vert = cv2.vconcat([img, img])
cv2.imshow("Vertical",vert)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Manipulated/Image3/vertical.JPG",vert)
#Horizontal Join
hor = cv2.hconcat([img, img])
cv2.imshow("Horizontal",hor)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Manipulated/Image3/horizontal.JPG",hor)
       
