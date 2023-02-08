import cv2
import numpy as np
import poseModule as pm

vdo=cv2.VideoCapture("/home/sanisha/Downloads/computer_vision/Full body tracking/squat.mp4")


detector=pm.poseDetector()

count=0
direction=0        #0 means half cnt



while True:
    success,frame=vdo.read()

    frame=cv2.resize(frame,(1280,720))
    #frame passes to detector
    frame=detector.findPose(frame,draw=False)

    #body landmark location
    lm_list=detector.findPosition(frame,draw=False)
    #print(lm_list)

    if len(lm_list)!=0:
        angle1=detector.findAngle(frame,24,26,28)              #right leg angle   ,pass evens
        #print(angle1)
        angle2=detector.findAngle(frame,23,25,27)              #left leg angle , pass odds
        #print(angle2)
    

        low=40
        high=170

        #convert to percentage
        percentage=np.interp(angle1,(low,high),(0,100))
        print(percentage)

        #print(angle1, "==>",percentage)


        #count
        if percentage==100:             #downwords
            if direction==0:
                count+=0.5
                direction=1


        if percentage==0:
            if direction==1:           #1 means upward direction
                count+=0.5
                direction=0

        
                
        # print(count)

        cv2.putText(frame,str(int(count)),(40,100),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),3)          #count display

        #loading bar
        bar=np.interp(angle1,(low,high),(700,100))
        #print(bar)

        cv2.rectangle(frame,(1100,100),(1175,700),(0,255,0),4)                    #rectangle has 2 pnts 
        cv2.rectangle(frame,(1100,int(bar)),(1175,700),(0,255,0),cv2.FILLED)      #bar assigns to rect
        #show percent
        cv2.putText(frame,str(int(percentage)),(1090,75),cv2.FONT_HERSHEY_PLAIN,4,(0,0,255),4)




    cv2.imshow("counter",frame)
    if cv2.waitKey(1) & 0xFF==27:
        break