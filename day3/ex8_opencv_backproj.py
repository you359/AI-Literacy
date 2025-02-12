import cv2

src = cv2.imread('desert.jpg', cv2.IMREAD_COLOR)
x, y, w, h = cv2.selectROI(src)
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
roi = src_ycrcb[y:y+h, x:x+w]
hist = cv2.calcHist([roi], [1, 2], None, [128, 128], [0, 256, 0, 256])
backproj = cv2.calcBackProject([src_ycrcb], [1, 2], hist, [0, 256, 0, 256], 1)
dst = cv2.copyTo(src, backproj)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()