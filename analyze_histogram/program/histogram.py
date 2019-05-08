# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import glob
import cv2
import matplotlib.pyplot as plt

files = glob.glob("../pictures/table/*.png")

for img in files:

    image = cv2.imread(img)
plt.subplots_adjust(hspace=0.3)
plt.figure(figsize=(16,9))
plt.subplot(3,1,1)
plt.hist(image[:,:,0].ravel(), bins=256, density=True, range=(0, 255), fc="b")
plt.xlim(0, 255)
plt.ylim(0, 0.04)
plt.ylabel("Gradation of BLUE")

plt.subplot(3,1,2)
plt.hist(image[:,:,1].ravel(), bins=256, density=True, range=(0, 255), fc="g")
plt.xlim(0, 255)
plt.ylim(0, 0.04)
plt.ylabel("Gradation of GREEN")

plt.subplot(3,1,3)
plt.hist(image[:,:,2].ravel(), bins=256, density=True, range=(0, 255), fc="r")
plt.xlim(0, 255)
plt.ylim(0, 0.04)
plt.xlabel("Component of Color")
plt.ylabel("Gradation of RED")

plt.savefig(str(img)+".png")

plt.close()

print(img)
