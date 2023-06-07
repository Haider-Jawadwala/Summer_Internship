import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('Original/Group.jpeg.jpg')
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Crop
crop=img[10:500,10:240]
# Detect faces
faces = face_cascade.detectMultiScale(crop, 1.3, 2)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 1)
# Display the output
cv2.imshow('img', img)
cv2.waitKey()
cv2.imwrite("Manipulated/Image2/Face_Detect.JPG",img)

