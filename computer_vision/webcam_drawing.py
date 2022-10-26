import cv2  
from datetime import datetime


def get_time():
    return datetime.now().strftime("%H:%M:%S")

webcam = cv2.VideoCapture(0) # video capturing and 0 meanslive camera or it will decode ur data through first camera  , 1 means usb camera


while webcam.isOpened():

    status, img = webcam.read() 
    if not status:
        print("Camera not working")
        break
    h,w,_ = img.shape
    img = cv2.resize(img, (w*2,h*2))
    msg = "camera 0 : Live Feed"
    pos = (10,30)
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (0,255,0) #bgr
    cv2.putText(img, msg, pos, font , 1 ,color , 2)
    cv2.putText(img, get_time(),(10,60),font, .5, color, 2)


    cv2.imshow("webcam",img)  #frame is a numpy array so we don't use print()
    #press esc to exit
    if cv2.waitKey(5) == 27: # 1ms delay 
        break
    webcam.release()
    cv2.destroyAllWindows()