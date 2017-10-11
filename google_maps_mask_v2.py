
import numpy as np
from motionless import CenterMap
import skimage.io
from skimage import color
from skimage.color import rgb2gray
from PIL import Image
import urllib.request
import io
from skimage import exposure

#39.030236,-3.3761257
#38.321221,-3.5573312
#lat=38.6038808, lon=-3.4694234
cmap = CenterMap(lat=38.0092846, lon=-4.3255341, size_x=640, size_y=640, zoom=18, scale=2)
URL = cmap.generate_url()
URL += "&style=feature:all|element:labels|visibility:off"

with urllib.request.urlopen(URL) as url:
    f = io.BytesIO(url.read())

img = np.array(Image.open(f).convert("RGB"))
img = rgb2gray(img)
skimage.io.imshow(img)
skimage.io.show()

threshold = 160
mask = (img > threshold - 10) & (img < threshold + 10) 

# skimage.io.imshow(mask)
# skimage.io.show()
#'lng': -4.3255341, 'lat': 38.0092846
cmap_sat = CenterMap(lat=38.0092846, lon=-4.3255341, maptype='satellite', size_x=640, size_y=640, zoom=18, scale=2)
img_sat = skimage.io.imread(cmap_sat.generate_url())

skimage.io.imshow(img_sat)
skimage.io.show()

# img_sat[np.invert(mask)] = [0, 0, 0]
# skimage.io.imshow(img_sat)
# skimage.io.show()

alpha = .6

color_mask = np.zeros(img_sat.shape)
color_mask[mask] = [255, 0, 0]
skimage.io.imshow(color_mask)
skimage.io.show()

# color_mask_hsv = color.rgb2hsv(color_mask)
# img_hsv = color.rgb2hsv(img_sat)

# img_hsv[..., 0] = color_mask_hsv[..., 0]
# img_hsv[..., 1] = color_mask_hsv[..., 1] * alpha

# img_masked = color.hsv2rgb(img_hsv)

img_sat[mask] = alpha * img_sat[mask] + (1 - alpha) * color_mask[mask]
img_sat = exposure.rescale_intensity(img_sat)

skimage.io.imshow(img_sat)
skimage.io.show()
