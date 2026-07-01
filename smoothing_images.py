import cv2
import numpy as np

img_filter = cv2.imread("filter.jpg")
img_median = cv2.imread("median.jpg")
img_bilateral = cv2.imread("bilateral.jpg")

blur = cv2.blur(img_filter, (5, 5))  # Ortalama (Box) Blur
blur_g = cv2.GaussianBlur(img_filter, (5, 5), cv2.BORDER_DEFAULT)  # Gaussian Blur
blur_m = cv2.medianBlur(img_median, 5)  # Median Blur
blur_b = cv2.bilateralFilter(img_bilateral, 9, 95, 95)  # Bilateral Filter

cv2.imshow("Original Bilateral", img_bilateral)
cv2.imshow("Box Blur", blur)
cv2.imshow("Gaussian Blur", blur_g)
cv2.imshow("Median Blur", blur_m)
cv2.imshow("Bilateral Blur", blur_b)

cv2.waitKey(0)
cv2.destroyAllWindows()
