# feature extraction
# from PIL import Image
import numpy
from scipy import misc
import scipy
from sklearn.feature_extraction import image
import matplotlib.pyplot as plt

mondrian = misc.imread("images/composition-2-1922.jpg")

patches = image.extract_patches_2d(mondrian,(10,10))
new_mondrian = image.reconstruct_from_patches_2d(patches, (512,512,3))
# im = plt.imshow(new_mondrian)
scipy.misc.imsave("new_mondrian.jpg",new_mondrian)

## THIS DIDN'T WORK AND ALSO WE CAN USE SOMEONE ELSE'S IMAGE PROCESSING
# im = Image.open("images/composition-2-1922.jpg") #Can be many different formats.
# pix = im.load()
# print im.size #Get the width and hight of the image for iterating over
# size = im.size


# pixelarray = numpy.empty([size[0]*1],dtype=dict)
# pixelarray = []
# count = 0

# for y in range(0,1):
#     for x in range(0,size[0]):
#         # initialize neighbor values for border pixels
#         neighbor1,neighbor2,neighbor3,neighbor4 = (255,255,255),(255,255,255),(255,255,255),(255,255,255)

#         # print pix[x,y] #Get the RGBA Value of the a pixel of an image
#         color = pix[x,y]
#         if y > 0:
#             neighbor1 = pix[x,y-1]
#         if x < size[0]-1:
#             neighbor2 = pix[x+1,y]
#         if y < size[1]-1:
#             neighbor3 = pix[x,y+1]
#         if x > 0:
#             neighbor4 = pix[x-1,y]
#         colors = {
#             "x": x,
#             "y": y,
#             "color": color,
#             "neighbor1": neighbor1,
#             "neighbor2": neighbor2,
#             "neighbor3": neighbor3,
#             "neighbor4": neighbor4,
#         }

#         # colors = str(x) + "," + str(y) + "," + str(color) + "," + str(neighbor1) + "," + str(neighbor2) + "," + str(neighbor3) + "," + str(neighbor4)

#         pixelarray.append(colors)
#         # pixelarray[count] = colors
#         print count
#         print pixelarray[count]
#         count = count + 1


## this doesn't work!
# features = DictVectorizer()
# features.fit_transform(pixelarray).toarray()
# print features