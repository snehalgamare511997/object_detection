import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('test_images/69614005')
rows,cols=img.Shape
pt1=np.flot32([[50,50],[200,50],[50,200]])
pt2=np.flot32([[10,100],[200,50],[100,250]])
matrix=cv2.getAffineTransform(pt1,pt2)
new_img=cv2.warpAffine(img,matrix,(cols,rows))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(new_img),plt.title('Output')
plt.show()
