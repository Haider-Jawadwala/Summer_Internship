import cv2
import numpy as np
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img= cv2.imread(r'Original/try4.jpg')
#GRAYSCALE
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img= cv2.bitwise_not(img)
img = img[220:500, 490:1400]
#Normalize
norm_img = np.zeros((img.shape[0], img.shape[1]))
img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
#skew
image_center = tuple(np.array(img.shape[1::-1]) / 2)
rot_mat = cv2.getRotationMatrix2D(image_center, -10, 1.0)
img = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)
img = img[0:245, 0:610]
cv2.imwrite("Manipulated/OCR4.JPG",img)
print(pytesseract.image_to_string(img))
       
