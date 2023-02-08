
import cv2
import numpy as np
import poseModule as pm
import pyttsx3

engine=pyttsx3.init()

vdo=cv2.VideoCapture("/home/sanisha/Downloads/computer_vision/Full body tracking/pushups.mp4")


detector=pm.poseDetector()

count=0
direction=0    
prev_val=0    



while True:
    success,frame=vdo.read()

    frame=cv2.resize(frame,(1280,720))
    
    #body tracking
    frame=detector.findPose(frame,draw=False)

    #body landmark location
    lm_list=detector.findPosition(frame,draw=False)
    

    if len(lm_list)!=0:
        angle1=detector.findAngle(frame,11,13,15)       #left hand          
        angle2=detector.findAngle(frame,12,14,16)        #right hand    

        
    
        low=200
        high=290
        
        #percentage of success of pushup
        percentage=np.interp(angle1,(low,high),(0,100))
        

         #bar to show pushup progress
        bar=np.interp(angle1,(low,high),(100,650))
    

        #pushup count
        if percentage==0:             
            if direction==1:
                count+=0.5
                direction=0


        if percentage==100:
            if direction==0:          
                count+=0.5
                direction=1

        
            
        cv2.putText(frame,"Push-ups:"+str(int(count)),(30,70),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,0),3)          #count display

        if (prev_val) < int(count):
            prev_val = int(count)
            engine.say(int(count))
            engine.runAndWait()
            

        cv2.rectangle(frame,(1100,100),(1150,650),(0,255,255),4)
        cv2.rectangle(frame,(1100,int(bar)),(1150,650),(0,255,255),cv2.FILLED)

        #to show percentage
        cv2.putText(frame,f'{int(percentage)}%',(1090,75),cv2.FONT_HERSHEY_PLAIN,4,(0,0,0),4)
        

    cv2.imshow("pushup_counter",frame)
    if cv2.waitKey(1) & 0xFF==27:
        break