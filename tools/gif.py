import cv2
img = cv2.imread("imgs/Hero.png")

h, w = img.shape[:2]
center = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(center, 45, 0.5)
rotated = cv2.warpAffine(img, M, (w, h))
cv2.imwrite("imgs/rotated.jpg", rotated)