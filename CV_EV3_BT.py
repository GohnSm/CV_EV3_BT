import cv2 as cv  
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

    
    n1=cv.inRange(cv.resize(cv.imread('1.png'),(64,64)),(254,254,254),(255,255,255)) 
    n2=cv.inRange(cv.resize(cv.imread('2.png'),(64,64)),(254,254,254),(255,255,255))  
    n3=cv.inRange(cv.resize(cv.imread('3.png'),(64,64)),(254,254,254),(255,255,255)) 
    n4=cv.inRange(cv.resize(cv.imread('4.png'),(64,64)),(254,254,254),(255,255,255))  
    n5=cv.inRange(cv.resize(cv.imread('5.png'),(64,64)),(254,254,254),(255,255,255))  
    n6=cv.inRange(cv.resize(cv.imread('6.png'),(64,64)),(254,254,254),(255,255,255)) 
    n7=cv.inRange(cv.resize(cv.imread('7.png'),(64,64)),(254,254,254),(255,255,255)) 
    n8=cv.inRange(cv.resize(cv.imread('8.png'),(64,64)),(254,254,254),(255,255,255)) 
    n9=cv.inRange(cv.resize(cv.imread('9.png'),(64,64)),(254,254,254),(255,255,255))   
    n10=cv.inRange(cv.resize(cv.imread('10.png'),(64,64)),(254,254,254),(255,255,255)) 
    n11=cv.inRange(cv.resize(cv.imread('11.png'),(64,64)),(254,254,254),(255,255,255)) 
    n12=cv.inRange(cv.resize(cv.imread('12.png'),(64,64)),(254,254,254),(255,255,255)) 
    
    cap=cv.VideoCapture(0)                                                                
    print('Press Q to quit')
    c=1
    while True:
         
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
                roImg=cv.inRange(roImg,(bmin,gmin,rmin),(bmax,gmax,rmax))
                #cv.imshow('detect',roImg)
                #cv.imshow('n',n1)
                #cv.imshow('n2',n7)
                


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

                for i in range(64):
                    for j in range(64):
                        if roImg[i][j] == n1[i][j]:
                            n1v+=1
                        if roImg[i][j] == n2[i][j]:
                            n2v+=1
                        if roImg[i][j] == n3[i][j]:
                            n3v+=1
                        if roImg[i][j] == n4[i][j]:
                            n4v+=1
                        if roImg[i][j] == n5[i][j]:
                            n5v+=1
                        if roImg[i][j] == n6[i][j]:
                            n6v+=1
                        if roImg[i][j] == n7[i][j]:
                            n7v+=1
                        if roImg[i][j] == n8[i][j]:
                            n8v+=1
                        if roImg[i][j] == n9[i][j]:
                            n9v+=1
                        if roImg[i][j] == n10[i][j]:
                            n10v+=1
                        if roImg[i][j] == n11[i][j]:
                            n11v+=1
                        if roImg[i][j] == n12[i][j]:
                            n12v+=1
                
            

            if c==1:
                cn='r'
                cr='17'
            if c==2:
                cn='g'
                cr='22'
            if c==3:
                cn='b'
                cr='24'
            if c==4:
                cn='y'
                cr='27'

            print(cn,'  ',n1v,' ',n2v,' ',n3v,' ',n4v,' ',n5v,' ',n6v,' ',n7v,' ',n8v,' ',n9v,' ',n10v,' ',n11v,' ',n12v)

            if n1v>3200:
                print('!!!!!!!!!!!!!!!!!!!!!!!    '+cn+' 1')
                gpio0=open('/sys/class/gpio/gpio'+cr+'/value','w')
                gpio0.write('1')
                gpio0.close
                gpio2=open('/sys/class/gpio/gpio3/value','w')
                gpio2.write('1')
                gpio2.close
                gpio3=open('/sys/class/gpio/gpio4/value','w')
                gpio3.write('1')
                gpio3.close
                time.sleep(3)
                gpio8=open('/sys/class/gpio/gpio'+cr+'/value','w')
                gpio8.write('0')
                gpio8.close
                gpio10=open('/sys/class/gpio/gpio3/value','w')
                gpio10.write('0')
                gpio10.close
                gpio11=open('/sys/class/gpio/gpio4/value','w')
                gpio11.write('0')
                break
            elif n2v>3160:
                print('!!!!!!!!!!!!!!!!!!!!!!!    '+cn+' 2')
                gpio0=open('/sys/class/gpio/gpio'+cr+'/value','w')
                gpio0.write('1')
                gpio0.close
                gpio1=open('/sys/class/gpio/gpio2/value','w')
                gpio1.write('1')
                gpio1.close
                gpio2=open('/sys/class/gpio/gpio3/value','w')
                gpio2.write('1')
                gpio2.close
                gpio3=open('/sys/class/gpio/gpio23/value','w')
                gpio3.write('1')
                gpio3.close
                gpio4=open('/sys/class/gpio/gpio14/value','w')
                gpio4.write('1')
                gpio4.close
                gpio5=open('/sys/class/gpio/gpio15/value','w')
                gpio5.write('1')
                gpio5.close
                time.sleep(3)
                gpio8=open('/sys/class/gpio/gpio'+cr+'/value','w')
                gpio8.write('0')
                gpio8.close
                gpio9=open('/sys/class/gpio/gpio2/value','w')
                gpio9.write('0')
                gpio9.close
                gpio10=open('/sys/class/gpio/gpio3/value','w')
                gpio10.write('0')
                gpio10.close
                gpio11=open('/sys/class/gpio/gpio23/value','w')
                gpio11.write('0')
                gpio11.close
                gpio12=open('/sys/class/gpio/gpio14/value','w')
                gpio12.write('0')
                gpio12.close
                gpio13=open('/sys/class/gpio/gpio15/value','w')
                gpio13.write('0')
                gpio13.close
                break
            elif n3v>3000:
                print('!!!!!!!!!!!!!!!!!!!!!!!    '+cn+' 3')
                gpio0=open('/sys/class/gpio/gpio'+cr+'/value','w')
                gpio0.write('1')
                gpio0.close
                gpio1=open('/sys/class/gpio/gpio2/value','w')
                gpio1.write('1')
                gpio1.close
                gpio2=open('/sys/class/gpio/gpio3/value','w')
                gpio2.write('1')
                gpio2.close
                gpio3=open('/sys/class/gpio/gpio4/value','w')
                gpio3.write('1')
                gpio3.close
                gpio4=open('/sys/class/gpio/gpio14/value','w')
                gpio4.write('1')
                gpio4.close
                gpio5=open('/sys/class/gpio/gpio15/value','w')
                gpio5.write('1')
                gpio5.close
                time.sleep(3)
                gpio8=open('/sys/class/gpio/gpio'+cr+'/value','w')
                gpio8.write('0')
                gpio8.close
                gpio9=open('/sys/class/gpio/gpio2/value','w')
                gpio9.write('0')
                gpio9.close
                gpio10=open('/sys/class/gpio/gpio3/value','w')
                gpio10.write('0')
                gpio10.close
                gpio11=open('/sys/class/gpio/gpio4/value','w')
                gpio11.write('0')
                gpio11.close
                gpio12=open('/sys/class/gpio/gpio14/value','w')
                gpio12.write('0')
                gpio12.close
                gpio13=open('/sys/class/gpio/gpio15/value','w')
                gpio13.write('0')
                gpio13.close
                break
            elif n4v>3000:
                print('!!!!!!!!!!!!!!!!!!!!!!!    '+cn+' 4')
                gpio0=open('/sys/class/gpio/gpio'+cr+'/value','w')
                gpio0.write('1')
                gpio0.close
                gpio2=open('/sys/class/gpio/gpio3/value','w')
                gpio2.write('1')
                gpio2.close
                gpio3=open('/sys/class/gpio/gpio4/value','w')
                gpio3.write('1')
                gpio3.close
                gpio5=open('/sys/class/gpio/gpio15/value','w')
                gpio5.write('1')
                gpio5.close
                gpio6=open('/sys/class/gpio/gpio18/value','w')
                gpio6.write('1')
                gpio6.close
                time.sleep(3)
                gpio8=open('/sys/class/gpio/gpio'+cr+'/value','w')
                gpio8.write('0')
                gpio8.close
                gpio10=open('/sys/class/gpio/gpio3/value','w')
                gpio10.write('0')
                gpio10.close
                gpio11=open('/sys/class/gpio/gpio4/value','w')
                gpio11.write('0')
                gpio11.close
                gpio13=open('/sys/class/gpio/gpio15/value','w')
                gpio13.write('0')
                gpio13.close
                gpio14=open('/sys/class/gpio/gpio18/value','w')
                gpio14.write('0')
                gpio14.close
                break
            elif n5v>3200:
                print('!!!!!!!!!!!!!!!!!!!!!!!    '+cn+' 5')
                gpio0=open('/sys/class/gpio/gpio'+cr+'/value','w')
                gpio0.write('1')
                gpio0.close
                gpio1=open('/sys/class/gpio/gpio2/value','w')
                gpio1.write('1')
                gpio1.close
                gpio3=open('/sys/class/gpio/gpio4/value','w')
                gpio3.write('1')
                gpio3.close
                gpio4=open('/sys/class/gpio/gpio14/value','w')
                gpio4.write('1')
                gpio4.close
                gpio5=open('/sys/class/gpio/gpio15/value','w')
                gpio5.write('1')
                gpio5.close
                gpio6=open('/sys/class/gpio/gpio18/value','w')
                gpio6.write('1')
                gpio6.close
                time.sleep(3)
                gpio8=open('/sys/class/gpio/gpio'+cr+'/value','w')
                gpio8.write('0')
                gpio8.close
                gpio9=open('/sys/class/gpio/gpio2/value','w')
                gpio9.write('0')
                gpio9.close
                gpio11=open('/sys/class/gpio/gpio4/value','w')
                gpio11.write('0')
                gpio11.close
                gpio12=open('/sys/class/gpio/gpio14/value','w')
                gpio12.write('0')
                gpio12.close
                gpio13=open('/sys/class/gpio/gpio15/value','w')
                gpio13.write('0')
                gpio13.close
                gpio14=open('/sys/class/gpio/gpio18/value','w')
                gpio14.write('0')
                gpio14.close
                break
            elif n6v>3000:
                print('!!!!!!!!!!!!!!!!!!!!!!!    '+cn+' 6')
                gpio0=open('/sys/class/gpio/gpio'+cr+'/value','w')
                gpio0.write('1')
                gpio0.close
                gpio1=open('/sys/class/gpio/gpio2/value','w')
                gpio1.write('1')
                gpio1.close
                gpio3=open('/sys/class/gpio/gpio4/value','w')
                gpio3.write('1')
                gpio3.close
                gpio4=open('/sys/class/gpio/gpio14/value','w')
                gpio4.write('1')
                gpio4.close
                gpio5=open('/sys/class/gpio/gpio15/value','w')
                gpio5.write('1')
                gpio5.close
                gpio6=open('/sys/class/gpio/gpio18/value','w')
                gpio6.write('1')
                gpio6.close
                gpio7=open('/sys/class/gpio/gpio23/value','w')
                gpio7.write('1')
                gpio7.close
                time.sleep(3)
                gpio8=open('/sys/class/gpio/gpio'+cr+'/value','w')
                gpio8.write('0')
                gpio8.close
                gpio9=open('/sys/class/gpio/gpio2/value','w')
                gpio9.write('0')
                gpio9.close
                gpio11=open('/sys/class/gpio/gpio4/value','w')
                gpio11.write('0')
                gpio11.close
                gpio12=open('/sys/class/gpio/gpio14/value','w')
                gpio12.write('0')
                gpio12.close
                gpio13=open('/sys/class/gpio/gpio15/value','w')
                gpio13.write('0')
                gpio13.close
                gpio14=open('/sys/class/gpio/gpio18/value','w')
                gpio14.write('0')
                gpio14.close
                gpio15=open('/sys/class/gpio/gpio23/value','w')
                gpio15.write('0')
                gpio15.close
                break
            elif n7v>3200:
                print('!!!!!!!!!!!!!!!!!!!!!!!    '+cn+' 7')
                gpio0=open('/sys/class/gpio/gpio'+cr+'/value','w')
                gpio0.write('1')
                gpio0.close
                gpio1=open('/sys/class/gpio/gpio2/value','w')
                gpio1.write('1')
                gpio1.close
                gpio2=open('/sys/class/gpio/gpio3/value','w')
                gpio2.write('1')
                gpio2.close
                gpio3=open('/sys/class/gpio/gpio4/value','w')
                gpio3.write('1')
                gpio3.close
                time.sleep(3)
                gpio8=open('/sys/class/gpio/gpio'+cr+'/value','w')
                gpio8.write('0')
                gpio8.close
                gpio9=open('/sys/class/gpio/gpio2/value','w')
                gpio9.write('0')
                gpio9.close
                gpio10=open('/sys/class/gpio/gpio3/value','w')
                gpio10.write('0')
                gpio10.close
                gpio11=open('/sys/class/gpio/gpio4/value','w')
                gpio11.write('0')
                gpio11.close
                break
            elif n8v>3000:
                print('!!!!!!!!!!!!!!!!!!!!!!!    '+cn+' 8')
                gpio0=open('/sys/class/gpio/gpio'+cr+'/value','w')
                gpio0.write('1')
                gpio0.close
                gpio1=open('/sys/class/gpio/gpio2/value','w')
                gpio1.write('1')
                gpio1.close
                gpio2=open('/sys/class/gpio/gpio3/value','w')
                gpio2.write('1')
                gpio2.close
                gpio3=open('/sys/class/gpio/gpio4/value','w')
                gpio3.write('1')
                gpio3.close
                gpio4=open('/sys/class/gpio/gpio14/value','w')
                gpio4.write('1')
                gpio4.close
                gpio5=open('/sys/class/gpio/gpio15/value','w')
                gpio5.write('1')
                gpio5.close
                gpio6=open('/sys/class/gpio/gpio18/value','w')
                gpio6.write('1')
                gpio6.close
                gpio7=open('/sys/class/gpio/gpio23/value','w')
                gpio7.write('1')
                gpio7.close
                time.sleep(3)
                gpio8=open('/sys/class/gpio/gpio'+cr+'/value','w')
                gpio8.write('0')
                gpio8.close
                gpio9=open('/sys/class/gpio/gpio2/value','w')
                gpio9.write('0')
                gpio9.close
                gpio10=open('/sys/class/gpio/gpio3/value','w')
                gpio10.write('0')
                gpio10.close
                gpio11=open('/sys/class/gpio/gpio4/value','w')
                gpio11.write('0')
                gpio11.close
                gpio12=open('/sys/class/gpio/gpio14/value','w')
                gpio12.write('0')
                gpio12.close
                gpio13=open('/sys/class/gpio/gpio15/value','w')
                gpio13.write('0')
                gpio13.close
                gpio14=open('/sys/class/gpio/gpio18/value','w')
                gpio14.write('0')
                gpio14.close
                gpio15=open('/sys/class/gpio/gpio23/value','w')
                gpio15.write('0')
                gpio15.close
                break
            elif n9v>3000:
                print('!!!!!!!!!!!!!!!!!!!!!!!    '+cn+' 9')
                gpio0=open('/sys/class/gpio/gpio'+cr+'/value','w')
                gpio0.write('1')
                gpio0.close
                gpio1=open('/sys/class/gpio/gpio2/value','w')
                gpio1.write('1')
                gpio1.close
                gpio2=open('/sys/class/gpio/gpio3/value','w')
                gpio2.write('1')
                gpio2.close
                gpio3=open('/sys/class/gpio/gpio4/value','w')
                gpio3.write('1')
                gpio3.close
                gpio4=open('/sys/class/gpio/gpio14/value','w')
                gpio4.write('1')
                gpio4.close
                gpio5=open('/sys/class/gpio/gpio15/value','w')
                gpio5.write('1')
                gpio5.close
                gpio6=open('/sys/class/gpio/gpio18/value','w')
                gpio6.write('1')
                gpio6.close
                time.sleep(3)
                gpio8=open('/sys/class/gpio/gpio'+cr+'/value','w')
                gpio8.write('0')
                gpio8.close
                gpio9=open('/sys/class/gpio/gpio2/value','w')
                gpio9.write('0')
                gpio9.close
                gpio10=open('/sys/class/gpio/gpio3/value','w')
                gpio10.write('0')
                gpio10.close
                gpio11=open('/sys/class/gpio/gpio4/value','w')
                gpio11.write('0')
                gpio11.close
                gpio12=open('/sys/class/gpio/gpio14/value','w')
                gpio12.write('0')
                gpio12.close
                gpio13=open('/sys/class/gpio/gpio15/value','w')
                gpio13.write('0')
                gpio13.close
                gpio14=open('/sys/class/gpio/gpio18/value','w')
                gpio14.write('0')
                gpio14.close
                break
            elif n10v>3000:
                print('!!!   10 ',cn)

                #GPIO.output(4,1)
                #time.sleep(4)
                #GPIO.output(4,0)
            elif n11v>3000:
                print('!!!   11 ',cn)

                #GPIO.output(4,1)
                #time.sleep(4)
                #GPIO.output(4,0)
            elif n12v>3000:
                print('!!!   12 ',cn)

                #GPIO.output(4,1)
                #time.sleep(4)
                #GPIO.output(4,0)
            

                
            
            #if (c==1) or (c==2) or (c==3):
                #c+=1
                #break
            # if c==4:
                # c=1
                # break
            
            #if cv.waitKey(1)==ord("q"):
                
                #break
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