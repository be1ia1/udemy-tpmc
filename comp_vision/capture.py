import cv2
from time import sleep

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    check, frame = video.read()

    # print(check)
    # print(frame)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # sleep(3)
    cv2.imshow('Capturing', gray)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()