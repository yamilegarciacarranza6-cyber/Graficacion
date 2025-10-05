import cv2 as cv
import numpy as np

width, height = 500, 500  
x, y = 100, 100
dx, dy = 5, 3  
radius = 20  

while True:
    img = np.ones((height, width, 3), dtype=np.uint8) * 255  
    cv.circle(img, (x, y), radius, (0, 234, 21), -1)
    cv.imshow("img", img)
    x += dx
    y += dy
    if x - radius <= 0 or x + radius >= width:
        dx = -dx
    if y - radius <= 0 or y + radius >= height:
        dy = -dy
    if cv.waitKey(30) & 0xFF == 27:
        break

cv.destroyAllWindows()
