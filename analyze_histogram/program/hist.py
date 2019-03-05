# Python 3.7.1
# OpenCV 4.0.0.21

import cv2
import matplotlib.pyplot as plt

dirpath = "../pictures/plant_aegis/"
print("input image file name")
filename = input()
filepath = dirpath+filename
print(filepath)

def show_histogram(image):
	# gray scale
	if image.ndim == 2:
		plt.hist(image.lavel(), bins=256, density=True, range=(0, 255), fc="k")
		plt.savefig("test.png")

	# color
	elif image.ndim == 3:
		plt.subplots_adjust(hspace=0.3)
		plt.figure(figsize=(16,9))

		plt.subplot(3,1,1)
		plt.hist(image[:,:,0].ravel(), bins=256, density=True, range=(0, 255), fc="b")
		plt.xlim(0, 255)
		plt.ylim(0, 0.02)

		plt.subplot(3,1,2)
		plt.hist(image[:,:,1].ravel(), bins=256, density=True, range=(0, 255), fc="g")
		plt.xlim(0, 255)
		plt.ylim(0, 0.02)

		plt.subplot(3,1,3)
		plt.hist(image[:,:,2].ravel(), bins=256, density=True, range=(0, 255), fc="r")
		plt.xlim(0, 255)
		plt.ylim(0, 0.02)

		plt.savefig("test.png")

if __name__ == "__main__":
	image = cv2.imread(filepath)
	show_histogram(image)
