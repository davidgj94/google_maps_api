import urllib.request, json 
origin = "37.9201552,-4.78568"
destination = "37.9472249,-4.5086721"
waypoints = "38.0141671,-4.3226138|38.0141671,-4.3226138|38.0141671,-4.3226138|38.01088,-3.9519901|38.1632843,-3.8496799|38.2501007,-3.8315636|38.2851714,-3.6970713"
URL = "https://maps.googleapis.com/maps/api/directions/json?origin=" + origin + "&destination=" + destination
URL += "&waypoints=" + waypoints
with urllib.request.urlopen(URL) as url:
    data = json.loads(url.read().decode())
num_steps = 0
for leg in data['routes'][0]['legs']:
	for step in leg['steps']:
		num_steps += 1
		print(step['start_location'])
		print(step['end_location'])
print(num_steps)

	

