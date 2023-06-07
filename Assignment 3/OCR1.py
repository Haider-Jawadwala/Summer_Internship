import cv2
import numpy as np
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img= cv2.imread(r'Original/try1.jpg')
#Noise
#img= cv2.fastNlMeansDenoisingColored(img, None, 2, 7, 7, 15)
#GRAYSCALE
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = img[217:250, 200:350]
#Normalize
norm_img = np.zeros((img.shape[0], img.shape[1]))
img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
#thresh
#_ ,img = cv2.threshold(img,120,225,cv2.THRESH_BINARY)
#erode
#kernel = np.ones((2, 2), np.uint8)
#img = cv2.erode(img, kernel, iterations=1)
#img = cv2.dilate(img, kernel, iterations=1)
cv2.imwrite("Manipulated/OCR1.JPG",img)

print(pytesseract.image_to_string(img))
       
