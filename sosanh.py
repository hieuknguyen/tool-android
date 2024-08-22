import cv2
import numpy as np


path = r'C:/Users/nguye/Downloads/a/large_image.png'
path1 = r'C:/Users/nguye/Downloads/a/a.png'
img = cv2.imread(path)
img1 = cv2.imread(path1)

result = cv2.matchTemplate(img, img1, cv2.TM_CCOEFF_NORMED)


threshold = 0.9
loc = np.where(result >= threshold)


if len(loc[0]) > 0:
    print("true")
else:
    print("false")
