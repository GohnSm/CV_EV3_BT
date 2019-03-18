import cv2 as cv
import numpy
#import RPIO
#import serial
import time
#import EV3BT

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(4, GPIO.OUT)

#hmm= 'n'
hmm=input('Change settings? y/n ')

while hmm == 'y':
    selcol=input('Select color (r=1/g=2/b=3/y=4) ')
    print('press esc to save')
    def nothing(x):
        pass
    cap=cv.VideoCapture(0)
    cv.namedWindow('result')  

    cv.createTrackbar('blur','result',1,50,nothing)
    cv.createTrackbar('erode','result',1,50,nothing)
    cv.createTrackbar('erodep','result',1,50,nothing)
    cv.createTrackbar('dilate','result',1,50,nothing)
    cv.createTrackbar('dilatep','result',1,50,nothing)

    cv.createTrackbar('rmin','result',0,255,nothing)
    cv.createTrackbar('gmin','result',0,255,nothing)
    cv.createTrackbar('bmin','result',0,255,nothing)

    cv.createTrackbar('rmax','result',255,255,nothing)
    cv.createTrackbar('gmax','result',255,255,nothing)
    cv.createTrackbar('bmax','result',255,255,nothing)

    while(True):
        ret,frame=cap.read()
        hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)                                              

       
        rmin=cv.getTrackbarPos('rmin','result')
        gmin=cv.getTrackbarPos('gmin','result')
        bmin=cv.getTrackbarPos('bmin','result')

        rmax=cv.getTrackbarPos('rmax','result')
        gmax=cv.getTrackbarPos('gmax','result')
        bmax=cv.getTrackbarPos('bmax','result')

        blur=cv.getTrackbarPos('blur','result')
        erode=cv.getTrackbarPos('erode','result')
        erodep=cv.getTrackbarPos('erodep','result')
        dilate=cv.getTrackbarPos('dilate','result')
        dilatep=cv.getTrackbarPos('dilatep','result')

        hsv=cv.blur(hsv,(int(blur),int(blur)))                                              

        mask=cv.inRange(hsv,(bmin,gmin,rmin),(bmax,gmax,rmax))                                
        masker= cv.erode(mask,(int(erode),int(erode)),iterations=int(erodep))                 
        maskdi= cv.dilate(masker,(int(dilate),int(dilate)),iterations=int(dilatep))            
        cv.imshow('mask',maskdi)                                                              

        result=cv.bitwise_and(frame,frame, mask = maskdi)                                     
        cv.imshow('result',result)                                                             

        if cv.waitKey(1)== 27:                                                                
            break
    sc=str(selcol)
    rang = open('range'+sc+'.txt','w')
    rang.write(str(cv.getTrackbarPos('rmin','result'))+'\n')
    rang.write(str(cv.getTrackbarPos('gmin','result'))+'\n')
    rang.write(str(cv.getTrackbarPos('bmin','result'))+'\n')
    rang.write(str(cv.getTrackbarPos('rmax','result'))+'\n')
    rang.write(str(cv.getTrackbarPos('gmax','result'))+'\n')
    rang.write(str(cv.getTrackbarPos('bmax','result'))+'\n')
    rang.write(str(cv.getTrackbarPos('blur','result'))+'\n')
    rang.write(str(cv.getTrackbarPos('erode','result'))+'\n')
    rang.write(str(cv.getTrackbarPos('erodep','result'))+'\n')
    rang.write(str(cv.getTrackbarPos('dilate','result'))+'\n')
    rang.write(str(cv.getTrackbarPos('dilatep','result'))+'\n')
    rang.close()
    cap.release()
    cv.destroyAllWindows()

    hmm=input('Continue? y/n ')



if hmm == 'n':

    gpio1=open('/sys/class/gpio/gpio2/value','w')
    gpio1.write('0')
    gpio1.close
    gpio2=open('/sys/class/gpio/gpio3/value','w')
    gpio2.write('0')
    gpio2.close
    gpio1=open('/sys/class/gpio/gpio4/value','w')
    gpio1.write('0')
    gpio1.close
    gpio2=open('/sys/class/gpio/gpio17/value','w')
    gpio2.write('0')
    gpio2.close
    gpio1=open('/sys/class/gpio/gpio27/value','w')
    gpio1.write('0')
    gpio1.close
    gpio2=open('/sys/class/gpio/gpio22/value','w')
    gpio2.write('0')
    gpio2.close
    gpio1=open('/sys/class/gpio/gpio14/value','w')
    gpio1.write('0')
    gpio1.close
    gpio2=open('/sys/class/gpio/gpio15/value','w')
    gpio2.write('0')
    gpio2.close
    gpio1=open('/sys/class/gpio/gpio18/value','w')
    gpio1.write('0')
    gpio1.close
    gpio2=open('/sys/class/gpio/gpio23/value','w')
    gpio2.write('0')
    gpio2.close
    gpio1=open('/sys/class/gpio/gpio24/value','w')
    gpio1.write('0')
    gpio1.close 

    
    n1=cv.inRange(cv.resize(cv.imread('1.png'),(64,64)),(0,0,0),(2,2,2)) 
    n2=cv.inRange(cv.resize(cv.imread('2.png'),(64,64)),(0,0,0),(2,2,2))  
    n3=cv.inRange(cv.resize(cv.imread('3.png'),(64,64)),(0,0,0),(2,2,2)) 
    n4=cv.inRange(cv.resize(cv.imread('4.png'),(64,64)),(0,0,0),(2,2,2))  
    n5=cv.inRange(cv.resize(cv.imread('5.png'),(64,64)),(0,0,0),(2,2,2))  
    n6=cv.inRange(cv.resize(cv.imread('6.png'),(64,64)),(0,0,0),(2,2,2)) 
    n7=cv.inRange(cv.resize(cv.imread('7.png'),(64,64)),(0,0,0),(2,2,2)) 
    n8=cv.inRange(cv.resize(cv.imread('8.png'),(64,64)),(0,0,0),(2,2,2)) 
    n9=cv.inRange(cv.resize(cv.imread('9.png'),(64,64)),(0,0,0),(2,2,2))   
    n10=cv.inRange(cv.resize(cv.imread('10.png'),(64,64)),(0,0,0),(2,2,2)) 
    n11=cv.inRange(cv.resize(cv.imread('11.png'),(64,64)),(0,0,0),(2,2,2)) 
    n12=cv.inRange(cv.resize(cv.imread('12.png'),(64,64)),(0,0,0),(2,2,2)) 
    
    cap=cv.VideoCapture(0)                                                                
    print('Press Q to quit')
    c=1
    while True:
        
        if c==1:
            cn='r'
        if c==2:
            cn='g'
        if c==3:
            cn='b'
        if c==4:
            cn='y'
        
        cs= str(c)
        rang = open('range'+cs+'.txt','r')                  
        rmin=int(str(rang.readline()).replace('\n',''))
        gmin=int(str(rang.readline()).replace('\n',''))
        bmin=int(str(rang.readline()).replace('\n',''))
        rmax=int(str(rang.readline()).replace('\n',''))
        gmax=int(str(rang.readline()).replace('\n',''))
        bmax=int(str(rang.readline()).replace('\n',''))
        blur=int(str(rang.readline()).replace('\n',''))
        erode=int(str(rang.readline()).replace('\n',''))
        erodep=int(str(rang.readline()).replace('\n',''))
        dilate=int(str(rang.readline()).replace('\n',''))
        dilatep=int(str(rang.readline()).replace('\n',''))
        rang.close()

        ret=True
        while (ret==True):	
            ret,frame=cap.read()                                                           
            #cv.imshow("Frame",frame)                                                           
            
            hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
            framec=hsv.copy()
            hsv=cv.blur(hsv,(int(blur),int(blur)))                                           

            mask=cv.inRange(hsv,(bmin,gmin,rmin),(bmax,gmax,rmax))                               
            mask=cv.erode(mask,(int(erode),int(erode)),iterations=int(erodep))                  
            mask=cv.dilate(mask,(int(dilate),int(dilate)),iterations=int(dilatep))              
            #cv.imshow('mask',mask)                                                                 

            contours=cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
            contours=contours[0]
      
            result=cv.bitwise_and(frame,frame, mask = mask)                                        
            #cv.imshow('result',result)

            n1v=0
            n2v=0
            n3v=0
            n4v=0
            n5v=0
            n6v=0
            n7v=0
            n8v=0
            n9v=0
            n10v=0
            n11v=0
            n12v=0 
            if len(contours) != 0:
                
                contours=sorted(contours,key=cv.contourArea,reverse=True)
                cv.drawContours(frame,contours,0,(255,0,255),3)
                #cv.imshow('contours',frame)
                (x,y,w,h)=cv.boundingRect(contours[0])
                cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                #cv.imshow('rect',frame)
                roImg=framec[y:y+h,x:x+w]
                roImg=cv.resize(roImg,(64,64))
                #cv.imshow('before',roImg)
                #roImg=cv.inRange(roImg,(bmin,gmin,rmin),(bmax,gmax,rmax))
                #cv.imshow('detect',roImg)
                #cv.imshow('n',n1)
                #cv.imshow('n2',n7)
                roImg=cv.cvtColor(roImg,cv.COLOR_BGR2GRAY)
                print(' ')
                print(' ')
                print(cn)
                if roImg.any() !=0:
                    for o in range(1,10):
                        print(o)
                        template=cv.cvtColor(cv.imread(str(o)+'.png'),cv.COLOR_BGR2GRAY)
                        resu=cv.matchTemplate(roImg,template,cv.TM_CCOEFF_NORMED)
                        minv,maxv,minl,maxl=cv.minMaxLoc(resu)
                        print(minv,maxv,minl,maxl)
                        print(' ')
                        #print(cn+' ',int(o))
                        #print(minv,' ',maxv,' ',minl,' ',maxl)
                        if (minv>100000) and (minv<150000):
                            print('!!!!!!!!!!!!!!!!!!!!!!!    '+cn+' ',int(o))
            break
            if cv.waitKey(1)== ord('q'):
                break
        if int(c) == 1:
            c=2
        elif int(c) == 2:
            c=3
        elif int(c) == 3:
            c=4
        elif int(c) == 4:
            c=1
        
        
            
    cap.release()
    cv.destroyAllWindows()