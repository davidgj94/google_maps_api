from motionless import CenterMap
from skimage.color import rgb2gray
from scipy import ndimage as ndi
from PIL import Image
import requests
import numpy as np
from io import StringIO
from skimage import io


cmap = CenterMap(lat=38.6038808, lon=-3.4694234, size_x=640, size_y=640, zoom=18, scale=2, style="feature:all|element:labels|visibility:off")
cmap_sat = CenterMap(lat=38.6038808, lon=-3.4694234, maptype='satellite', size_x=640, size_y=640, zoom=18, scale=2)

url = cmap.generate_url()
url += "&style=feature:all|element:labels|visibility:off"
# response = requests.get(url)
# img = np.array(Image.open(StringIO(response.content)))
# img_sat = io.imread(cmap_sat.generate_url())
# img = io.imread("https://maps.googleapis.com/maps/api/staticmap?maptype=roadmap&center=38.7012335,-3.4256068&zoom=19&size=1280x1280&style=feature:all|element:labels|visibility:off&key=AIzaSyDvgF0JSBrlYLDzY7pPqtcBSgGslmaAlzw")
img = io.imread(url)
img_gray = rgb2gray(img)

io.imshow(img_gray)
io.show()

# threshold = threshold_otsu(img_gray)

# threshold = img_gray[1083,1108]

threshold = 0.86

mask = (img_gray > threshold - .005) & (img_gray < threshold + .005) 

io.imshow(mask)
io.show()


# mask = ndi.binary_fill_holes(mask)

# io.imshow(mask)
# io.show()
