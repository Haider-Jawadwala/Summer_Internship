import cv2
import numpy as np

#Read/Write
video = cv2.VideoCapture('Original/sample-1.mp4')
if (video.isOpened() == False): 
    print("Error reading video file")
    
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(video.get(cv2.CAP_PROP_FPS))
output = cv2.VideoWriter('Manipulated/Video_new.mp4', cv2.VideoWriter_fourcc(*'MJPG'), fps, (frame_width, frame_height))    
while(True):
    ret, frame = video.read()
    resize = cv2.resize(frame, (700, 500))
  
    if ret == True: 
        output.write(frame)
        cv2.imshow('Frame', resize)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else:
        break
video.release()
output.release()
cv2.destroyAllWindows()
       
