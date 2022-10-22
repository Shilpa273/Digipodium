import cv2 

webcam = cv2.VideoCapture(0)
while True:
    status, frame = webcam.read()
    if not status:
        print("Camera not workinf")
        break
    cv2.imshow("webcam",frame)
    #press esc to exit
    if cv2.waitkey(1) == 27: # 1ms delay
        break
    webcam.release()
    cv2.destroyAllWindows()