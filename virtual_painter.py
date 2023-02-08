import cv2
import numpy as np
import HandTrackingModule as htm

detector=htm.handDetector(detectionCon=0.85)

webcam=cv2.VideoCapture(0)

# set screen resolution
webcam.set(3,1280)
webcam.set(4,720)

#canvas creation
imgcanvas=np.zeros((720,1280,3),np.uint8)                 #uint8 ,a number format

drawcolor=(0,0,255)                                         #default color for starting

while True:
    #reading frame
    success,frame=webcam.read()
    #draw colored rectangles
    cv2.rectangle(frame,(0,0),(1280,120),(255,255,0),cv2.FILLED)

    cv2.rectangle(frame,(20,10),(220,100),(0,0,255),cv2.FILLED)
    cv2.rectangle(frame,(260,10),(450,100),(0,255,0),cv2.FILLED)
    cv2.rectangle(frame,(500,10),(690,100),(255,0,0),cv2.FILLED)
    cv2.rectangle(frame,(740,10),(930,100),(0,255,255),cv2.FILLED)
    cv2.rectangle(frame,(980,10),(1260,100),(255,255,255),cv2.FILLED)
    cv2.putText(frame,"ERASER",(1060,65),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),3)                      #labelled as eraser

#1.find hands

    frame=detector.findHands(frame)
    #landmark list: to detect hand position
    lm_list=detector.findPosition(frame,draw=False)
    # print(lm_list)

    if len(lm_list)!=0:
        x1,y1=lm_list[8][1:]                                     #except 1st value
        x2,y2=lm_list[12][1:]
        # print("index finger position",x1,y1)
        # print("middle finger position",x2,y2)

#2.check which finger is up or not
        fingers=detector.fingersUp()
        # print(fingers)


#3.selection mode.check index finger & middle finger is up

        if fingers[1] and fingers[2]:

            xp,yp= 0,0                                  #starting ,end pnt

            if y1<130:
                if 20<x1<240:
                    drawcolor=(0,0,255)                #red color
                    # print("red")
                
                elif  260<x1<480:
                    drawcolor=(0,255,0)               #draw color green
                    # print("green")
                
                elif 500<x1<720:
                    drawcolor=(255,0,0)
                    # print("blue")

                elif 740<x1<960:
                    drawcolor=(0,255,255)
                    # print("yellow")
                
                else:
                    drawcolor=(0,0,0)
                    print("Eraser")
                    
            cv2.rectangle(frame,(x1,y1),(x2,y2),drawcolor,cv2.FILLED)

            print("selection mode")

#4.drawing mode.index finger is up

        if fingers[1] and not fingers[2]:

            cv2.circle(frame,(x1,y1),10,drawcolor,thickness=-1)                 #fingertip acts as circle
            
            #starting pnt as index finger
            if xp==0 and yp==0:
                xp=x1
                yp=y1
            
            if drawcolor==(0,0,0):                #eraser condition
                cv2.line(frame,(xp,yp),(x1,y1),color=drawcolor,thickness=30)
                cv2.line(imgcanvas,(xp,yp),(x1,y1),color=drawcolor,thickness=30)
            else:
                cv2.line(frame,(xp,yp),(x1,y1),color=drawcolor,thickness=20)
                cv2.line(imgcanvas,(xp,yp),(x1,y1),color=drawcolor,thickness=20)

            
            xp,yp=x1,y1        #pnts assigned to x1,y1

            print("drawing mode")
    imggrey=cv2.cvtColor(imgcanvas,cv2.COLOR_BGR2GRAY)
    thresh,imgInv=cv2.threshold(imggrey,20,255,cv2.THRESH_BINARY_INV)
    imgInv=cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)

    #Bitwise operations
    frame=cv2.bitwise_and(frame,imgInv)
    frame=cv2.bitwise_or(frame,imgcanvas)



    # cv2.imshow("image",frame)
    # cv2.imshow("canvas",imgcanvas)

    #add img canvas & frame
    frame=cv2.addWeighted(frame,1,imgcanvas,0.5,0)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF==27:
        break
