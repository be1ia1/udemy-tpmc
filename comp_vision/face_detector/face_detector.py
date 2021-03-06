import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv2.imread('photo.jpg')
img = cv2.imread('news.jpg')
# cv2.imshow('Original', img)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, 
scaleFactor=1.08,
minNeighbors=5)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv2.imshow('Color', img)
# cv2.imshow('Gray', gray_img)
cv2.waitKey()
cv2.destroyAllWindows()


