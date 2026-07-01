#roi -> region of interest -> ilgi alanı
import cv2

img = cv2.imread("amiral.jpg")
#print(img.shape[:2])

roi = img[30:200 ,200:400]

cv2.imshow("araba", img)
cv2.imshow("ROİ:" ,roi)

cv2.waitKey(0)
cv2.destroyAllWindows()