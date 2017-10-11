import urllib.request, json 
with urllib.request.urlopen("https://maps.googleapis.com/maps/api/directions/json?origin=38.057358,%20-3.904601&destination=38.988962,%20-3.386459&waypoints=38.166380,%20-3.709047|38.332074,%20-3.543737|38.437385,%20-3.496714|38.508502,%20-3.496502|38.640925,%20-3.476919") as url:
    data = json.loads(url.read().decode())
for leg in data['routes'][0]['legs']:
	for step in leg['steps']:
		print(step['start_location'])
		print(step['end_location'])

	

