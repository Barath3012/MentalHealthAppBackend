import matplotlib.pyplot
import numpy
import copy
import math
import random
from mpmath import mpf
import numpy as np



# Part 1 - Gray scale
def createGrayScaleImage():


    # black = numpy.zeros((height, width), dtype=float)

    #make the variables global for access
    #global myImage,height,width


    myImage = matplotlib.pyplot.imread('flower.png')
    myImage2= copy.deepcopy(myImage)
    myImage3 = copy.deepcopy(myImage)

    height = myImage.shape[0]
    width = myImage.shape[1]

    #Iterate through the picture and add it into a 2 x 2 matrix called myImage
    for x in range(0, height - 1):

        for y in range(0, width - 1):

            #Get the RGBA values
            R, G, B, A = myImage[x][y]
            #print(R,G,B,A)



            # Average method
            #Get the average of the RGBA
            average = (R + G + B) / 3

            #Black and white scale Conversion

            averagePivot = 0.5
            if (average > averagePivot):
                myImage3[x][y] = [1.0,1.0,1.0,1.0] # [255,255,255,255]

            else:
                print(R,G,B)
                #print(x,y)
                myImage3[x][y] = [0.0,0.0,0.0,1.0]  # [0,0,0,0]

    #Show the image when it's done
    black_white_plot = matplotlib.pyplot.imshow(myImage3)
    matplotlib.pyplot.show()

    print("Success")

    myImage = matplotlib.pyplot.imread('flower.png')
    return
    height = myImage.shape[0]
    width = myImage.shape[1]
    RWeight,Gweight,Bweight = 1,0,0
    for x in range(0, height - 1):
        for y in range(0, width - 1):
            R, G, B, A = myImage[x][y]
            #R, G, B, A = int(R * 255), int(G * 255), int(B * 255), int(A*255)

            # Average method
            #gray_scale = (R + G + B) / 3

            #commenting the average method and replacing it with a better method for grayscaling
            gray_scale = float(RWeight * R + Gweight * G + Bweight * B)
            #print(R,G,B,A,gray_scale)

            myImage2[x][y] = [gray_scale,gray_scale,gray_scale,A]
            #myImage2[x][y]=myImage[x][y].astype(numpy.int32)
            #myImage2[x][y] = myImage2[x][y].astype(numpy.int32)


    img_grey_plot = matplotlib.pyplot.imshow(myImage2)
    #print(myImage)
    matplotlib.pyplot.show()


# Part 2 - Blurring an image
def blurTheImage():
    myImage = matplotlib.pyplot.imread('flower.png')
    myImage2 = copy.deepcopy(myImage)

    height = myImage.shape[0]
    width = myImage.shape[1]
    sumValues = 0

    R,G,B = [],[],[]

    for x in range(0, height - 1):
        R1=[]
        G1=[]
        B1=[]
        for y in range(0, width - 1):
            #myImage2[x][y] = [myImage2[x][y][i]/sumValues[i] for i in range(len(myImage2[x][y])-1)]
            R1.append(myImage[x][y][0])
            G1.append(myImage[x][y][1])
            B1.append(myImage[x][y][2])
        R.append(R1)
        G.append(G1)
        B.append(B1)
    thresh=3
    #print(R)
    for x in range(thresh//2, height - thresh//2 -1):
        #R1=[],G1=[],B1=[]
        for y in range(thresh//2, width - thresh//2 -1):
            if findAdjacentSum(R,thresh**2,startIndex=(x,y)) == 0:
                continue
            try:

                myImage2[x][y] = [myImage[x][y][0]/mpf(findAdjacentSum(R,thresh**2,startIndex=(x,y))),myImage[x][y][1]/mpf(findAdjacentSum(G,thresh**2,startIndex=(x,y))),myImage[x][y][2]/mpf(findAdjacentSum(B,thresh**2,startIndex=(x,y))),1.0]
            except:
                pass

        print(x)
    #return
    blur_plot = matplotlib.pyplot.imshow(myImage2)
    matplotlib.pyplot.show()

def newBlur():
    import operator

    myImage = matplotlib.pyplot.imread('flower.png')

    height = myImage.shape[0]
    width = myImage.shape[1]
    blur_image = copy.deepcopy(myImage)


    for x in range(0, height - 1):
        for y in range(0, width - 1):
            pixels_sum = (0, 0, 0)
            for pixel in [(x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x - 1, y), (x, y), (x + 1, y), (x - 1, y - 1),
                          (x, y - 1), (x + 1, y - 1)]:

                #pixels_sum=tuple(pixels_sum[0] + myImage[pixel[0]][pixel[1]][:3])
                pass


                #pixels_sum = tuple(map(operator.add, pixels_sum, tuple(myImage[pixel[0]][pixel[1]][:3])))

            pixels_sum = [pixels_sum[i]/9 for i in range(len(pixels_sum))]
            #print(tuple(map(operator.floordiv, pixels_sum, (9, 9, 9))))
            #blur_image[x][y] =  tuple(map(operator.floordiv, pixels_sum, (9, 9, 9))) + (1,)

            blur_image[x][y] = pixels_sum + [1]


    blur_plot = matplotlib.pyplot.imshow(blur_image)
    matplotlib.pyplot.show()

def findAdjacentSum(m,n,startIndex=None):
    import operator
    count = 0
    if not startIndex:
        x,y=len(m)//2,len(m[0])//2
    else:
        x,y=startIndex
    minx,miny = -1+x,-1+y
    maxx,maxy = 1+x,1+y
    sum=0
    directionx,directiony = 0,-1
    while count < n:

        #print(x,y,directionx,directiony,m[x][y])

        try:
            sum+= m[x][y]
        except:
            print(x,y)
        if x==minx and y==miny:
            minx-=1
            miny-=1
            directionx=0
            directiony=1

        else:
            if y == miny:
                miny -= 1
                directionx = -1
                directiony = 0

            elif y == maxy:
                maxy += 1
                directionx = 1
                directiony = 0

            if x == minx:
                minx -= 1
                directionx = 0
                directiony = 1

            elif x == maxx:
                maxx += 1
                directionx = 0
                directiony = -1


        x+=directionx
        y+=directiony
        count+=1
    return(sum)





if __name__ == "__main__":
    '''
    a = []
    count1=1
    for i in range(1,12):
       b=[]
       for j in range(1,12):
           b.append(count1)
           count1+=1
       a.append(b)

    print(a)
    for i in range(1,100):
        print(findAdjacentSum(a,i))
    '''
    blurTheImage()
