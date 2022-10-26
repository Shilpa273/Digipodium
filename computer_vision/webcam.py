import cv2 

webcam = cv2.VideoCapture(0) # video capturing and 0 means live camera or it will decode ur data through first camera  , 1 means usb camera


while webcam.isOpened():

    status, frame = webcam.read() 
    if not status:
        print("Camera not working")
        break
    cv2.imshow("webcam",frame)  #frame is a numpy array so we don't use print()
    #press esc to exit
    if cv2.waitKey(5) == 27: # 1ms delay
        break
    webcam.release()
    cv2.destroyAllWindows()