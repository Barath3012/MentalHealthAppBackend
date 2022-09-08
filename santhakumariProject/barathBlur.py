import numpy
import math
from main import findAdjacentSum
def multiplyGaussWithKernal(gauss,kernal):
    #please specify them with same dimensions
    return [[i*j for i,j in zip(gauss[k],kernal[k])] for k in range(len(gauss))]

def makeGaussianMatrix(n,sigma):
    if n%2==0:
        raise Exception("YOU CANNOT SPECIFY AN EVEN VALUE HERE !!!")
    return [[gaussianFilter(i-(n//2),j-(n//2),sigma) for i in range(n)] for j in range(n)]
def gaussianFilter(x,y,std):
    return 1/(2*math.pi*(std**2)) * math.e**(-((x**2 + y**2)/2*(std**2)))
if __name__ == "__main__":

    import matplotlib.pyplot
    import numpy as np

    myImage = matplotlib.pyplot.imread('flower.png')

    #print(myImage.shape)
    height = myImage.shape[0]
    width = myImage.shape[1]

    # Part 2 - Blurring
    # Blurring by average of pixels of 4 neighbors
    """Blurring of an image by setting each pixel’s value to the average of the four neighbours around it"""
    blur_image = np.copy(myImage)
    gauss = makeGaussianMatrix(3,0.8)
    print(gauss)
    quit()
    for x in range(3, height - 3):
        for y in range(3, width - 3):
            #blur_image[x][y] = findAdjacentSum(multiplyGaussWithKernal(gauss,myImage[x-1:x+2,y-1:y+2][:3]),9)
            a = [[np.array([i,j,k]) for i,j,k,l in L] for L in myImage[x-1:x+2,y-1:y+2]]
            blur_image[x][y][:3] = sum(sum(list(map(np.array,multiplyGaussWithKernal(gauss,a)))))
            #print("=========================")
            #print(sum(sum(list(map(np.array,multiplyGaussWithKernal(gauss,a))))))
            #print(list(map(np.array,multiplyGaussWithKernal(gauss,a))))
            #print("=========================")


            for i,j in enumerate(blur_image[x][y][:3]):

                if j > 1:
                    blur_image[x][y][i] = 1.0



    blur_plot = matplotlib.pyplot.imshow(blur_image)
    matplotlib.pyplot.show()






