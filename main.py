import cv2 
import time

trialNum = 1
nframes = 10 # num of pictures to take
interval = 1 # seconds

cap = cv2.VideoCapture(0) 

for i in range(nframes):
    ret, img = cap.read()
    cv2.imwrite('./Photos/img_'+str(trialNum).zfill(2)+'_'+str(i+1).zfill(4)+'.png', img)
    time.sleep(interval)

cap.release()