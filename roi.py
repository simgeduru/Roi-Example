import cv2
from matplotlib import pyplot as plt

resim = cv2.imread("file_path")

plt.imshow(resim)
plt.show()
roi = resim[46:450, 20:450]
cv2.imshow("roi", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()