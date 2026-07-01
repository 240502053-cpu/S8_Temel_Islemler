import cv2

img = cv2.imread("amiral.jpg")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("amiral BGR", img)
#cv2.imshow("amiral RGB", img_rgb)
#cv2.imshow("amiral HSV", img_hsv)
cv2.imshow("amiral GRAY", img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
