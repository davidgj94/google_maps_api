import numpy as np
from motionless import CenterMap
import skimage.io
from skimage import color
from skimage.color import rgb2gray
from PIL import Image
import urllib.request, json
import io
from skimage import exposure

def road_segmentation(coord):

	cmap = CenterMap(lat=coord[0], lon=coord[1], size_x=640, size_y=640, zoom=18, scale=2)
	URL = cmap.generate_url()
	URL += "&style=feature:all|element:labels|visibility:off"

	with urllib.request.urlopen(URL) as url:
	    f = io.BytesIO(url.read())

	img = np.array(Image.open(f).convert("RGB"))
	img = rgb2gray(img)

	cmap_sat = CenterMap(lat=coord[0], lon=coord[1], maptype='satellite', size_x=640, size_y=640, zoom=18, scale=2)
	img_sat = skimage.io.imread(cmap_sat.generate_url())

	threshold = 0.909
	mask = (img > threshold - .001) & (img < threshold + .001)
	mask = np.invert(mask)

	color_mask = np.zeros(img_sat.shape)
	color_mask[mask] = [255, 0, 0]

	alpha = .6
	blended = alpha * img_sat + (1 - alpha) * color_mask

	return exposure.rescale_intensity(blended)

def get_coord(coord_dict):
	return (coord_dict['lat'], coord_dict['lng'])

origin = "37.9201552,-4.78568"
destination = "37.9472249,-4.5086721"
waypoints = "38.0141671,-4.3226138|38.0141671,-4.3226138|38.0141671,-4.3226138|38.01088,-3.9519901|38.1632843,-3.8496799|38.2501007,-3.8315636|38.2851714,-3.6970713"
URL = "https://maps.googleapis.com/maps/api/directions/json?origin=" + origin + "&destination=" + destination
URL += "&waypoints=" + waypoints
print(URL)

with urllib.request.urlopen(URL) as url:
    data = json.loads(url.read().decode())

for leg in data['routes'][0]['legs']:
	for step in leg['steps']:
		coord = get_coord(step['start_location'])
		skimage.io.imsave(str(step['start_location']) + ".jpg", road_segmentation(coord))
		print("New image saved!!!")
		coord = get_coord(step['end_location'])
		skimage.io.imsave(str(step['end_location']) + ".jpg", road_segmentation(coord))
		print("New image saved!!!")


