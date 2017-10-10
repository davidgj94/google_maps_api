
import numpy as np
from motionless import CenterMap
from skimage import io as io2

cmap = CenterMap(lat=38.6038808, lon=-3.4694234, size_x=640, size_y=640, zoom=18, scale=2)

URL = cmap.generate_url()
URL += "&style=feature:all|element:labels|visibility:off"
print(URL)

# # req = urlopen('http://answers.opencv.org/upfiles/logo_2.png')
# # arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
# # print(arr.shape)

# img = io.imread(url)
# io.imshow(img)
# io.show()


from PIL import Image
import urllib.request
import io

with urllib.request.urlopen(URL) as url:
    f = io.BytesIO(url.read())

img = np.array(Image.open(f))
io2.imshow(img)
io2.show()
