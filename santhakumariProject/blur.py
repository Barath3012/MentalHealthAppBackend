# BlurImage.py
# Lab5: This program will blur the image using average of four neighbors and explore Gaussian blurring
# 27 June 2022

import matplotlib.pyplot
import numpy as np

myImage = matplotlib.pyplot.imread('flower.png')

print(myImage.shape)
height = myImage.shape[0]
width = myImage.shape[1]

# Part 2 - Blurring
# Blurring by average of pixels of 4 neighbors
"""Blurring of an image by setting each pixel’s value to the average of the four neighbours around it"""
blur_image = np.copy(myImage)
for x in range(0, height - 1):
    for y in range(0, width - 1):
        blur_image[x][y] = (myImage[x + 1][y] + myImage[x][y + 1] + myImage[x - 1][y] + myImage[x][y - 1]) / 4

# Show the image when it's done
blur_plot = matplotlib.pyplot.imshow(blur_image)
matplotlib.pyplot.show()

# Expansion of basic algorithm - with 8 neighbors
blur_image2 = np.copy(myImage)
for x in range(0, height - 1):
    for y in range(0, width - 1):
        pixels_sum = (0, 0, 0)
        R, G, B, A = myImage[x][y]
        for pixel in [(x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x - 1, y), (x, y), (x + 1, y), (x - 1, y - 1),
                      (x, y - 1), (x + 1, y - 1)]:
            pixels_sum = [pixels_sum[i] / 9 for i in range(len(pixels_sum))]
        blur_image2[x][y] = pixels_sum + [A]
blur_plot = matplotlib.pyplot.imshow(blur_image2)
matplotlib.pyplot.show()

# TO do - implement gaussian blurring with weightage
# https://datacarpentry.org/image-processing/06-blurring/#:~:text=In%20a%20Gaussian%20blur%2C%20the,pixel%20in%20the%20filtered%20image

































