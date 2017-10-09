from motionless import CenterMap
from skimage import io
from skimage.color import rgb2gray
import cv2
import numpy as np
from scipy import ndimage as ndi

cmap = CenterMap(lat=38.6038808, lon=-3.4694234, size_x=640, size_y=640, zoom=18, scale=2)
cmap_sat = CenterMap(lat=38.6038808, lon=-3.4694234, maptype='satellite', size_x=640, size_y=640, zoom=18, scale=2)

img = io.imread(cmap.generate_url())
img_sat = io.imread(cmap_sat.generate_url())

img_gray = rgb2gray(img)

io.imshow(img_gray)
io.show()

# threshold = threshold_otsu(img_gray)

threshold_1 = img_gray[1083,1108]
# threshold_2 = img_gray[1013,1123]
threshold_2 = 0.262

mask_1 = (img_gray > threshold_1 - .005) &  (img_gray < threshold_1 + .005) 
mask_2 = (img_gray > threshold_2 - .005) &  (img_gray < threshold_2 + .005) 

io.imshow(mask_1)
io.show()

io.imshow(mask_2)
io.show()

io.imshow(np.invert(mask_2))
io.show()

im2, contours, hierarchy = cv2.findContours(np.invert(mask_2).astype('uint8'), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
mask = cv2.drawContours(mask_1.astype('uint8'), contours, -1, 255, cv2.FILLED)


io.imshow(mask)
io.show()

mask = ndi.binary_fill_holes(mask)
# io.imsave("without rectangles.jpg", mask.astype(float))

io.imshow(mask)
io.show()




# # # io.imshow(img_sat)
# # # io.show()

# # io.imshow(img_gray)
# # io.show()

# # # io.imshow(mask)
# # # io.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import skimage.morphology, skimage.data

# labels = skimage.morphology.label(mask)
# labelCount = np.bincount(labels.ravel())
# background = np.argmax(labelCount)
# mask[labels != background] = 255
# plt.imshow(mask, cmap=plt.cm.gray)
# plt.show()