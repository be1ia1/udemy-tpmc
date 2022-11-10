import cv2
img = cv2.imread('galaxy.jpg', 0)
scale_percent = 50 #int(input('Enter scale percent:'))
new_size = int(img.shape[1] * scale_percent / 100), int(img.shape[0] * scale_percent / 100)
resized_img = cv2.resize(img, new_size)
cv2.imwrite('galaxy_resized.jpg', resized_img)
cv2.imshow('Galaxy', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
