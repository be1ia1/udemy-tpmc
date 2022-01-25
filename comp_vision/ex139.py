import cv2
import glob

files = glob.glob('sample_images/*')

for file in files:
    img = cv2.imread(file, 1)
    resized_img = cv2.resize(img, (100, 100))
    cv2.imwrite(file[:-4] + '_resized.jpg', resized_img)
