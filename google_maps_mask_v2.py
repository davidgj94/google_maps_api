
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
cmap = CenterMap(lat=37.9039882, lon=-4.7740557, size_x=640, size_y=640, zoom=18, scale=2)
URL = cmap.generate_url()
URL = "https://maps.googleapis.com/maps/api/staticmap?key=AIzaSyDvgF0JSBrlYLDzY7pPqtcBSgGslmaAlzw&center=38.043824,%20-3.985887&zoom=18&format=png&maptype=roadmap&style=element:geometry%7Ccolor:0x212121&style=element:labels%7Cvisibility:off&style=element:labels.icon%7Cvisibility:off&style=element:labels.text.fill%7Ccolor:0x757575&style=element:labels.text.stroke%7Ccolor:0x212121&style=feature:administrative%7Celement:geometry%7Ccolor:0x757575%7Cvisibility:off&style=feature:administrative.country%7Celement:labels.text.fill%7Ccolor:0x9e9e9e&style=feature:administrative.land_parcel%7Cvisibility:off&style=feature:administrative.locality%7Celement:labels.text.fill%7Ccolor:0xbdbdbd&style=feature:administrative.neighborhood%7Cvisibility:off&style=feature:poi%7Cvisibility:off&style=feature:poi%7Celement:labels.text.fill%7Ccolor:0x757575&style=feature:poi.park%7Celement:geometry%7Ccolor:0x181818&style=feature:poi.park%7Celement:labels.text.fill%7Ccolor:0x616161&style=feature:poi.park%7Celement:labels.text.stroke%7Ccolor:0x1b1b1b&style=feature:road%7Celement:geometry.fill%7Ccolor:0x2c2c2c&style=feature:road%7Celement:labels.icon%7Cvisibility:off&style=feature:road%7Celement:labels.text.fill%7Ccolor:0x8a8a8a&style=feature:road.arterial%7Celement:geometry%7Ccolor:0x373737&style=feature:road.highway%7Celement:geometry%7Ccolor:0x3c3c3c&style=feature:road.highway.controlled_access%7Celement:geometry%7Ccolor:0x4e4e4e&style=feature:road.local%7Celement:labels.text.fill%7Ccolor:0x616161&style=feature:transit%7Cvisibility:off&style=feature:transit%7Celement:labels.text.fill%7Ccolor:0x757575&style=feature:water%7Celement:geometry%7Ccolor:0x000000&style=feature:water%7Celement:labels.text.fill%7Ccolor:0x3d3d3d&size=640x640&scale=2"

with urllib.request.urlopen(URL) as url:
    f = io.BytesIO(url.read())

img = np.array(Image.open(f).convert("RGB"))
# img = rgb2gray(img)
skimage.io.imshow(exposure.rescale_intensity(img))
skimage.io.show()

threshold = 160
mask = (img > threshold - 10) & (img < threshold + 10) 

# skimage.io.imshow(mask)
# skimage.io.show()
#'lng': -4.3255341, 'lat': 38.0092846
cmap_sat = CenterMap(lat=37.9039882, lon=-4.7740557, maptype='satellite', size_x=640, size_y=640, zoom=18, scale=2)
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
