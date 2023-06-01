import urllib.request
import json

# URL of the JSON endpoint
url = "https://napa.mawasiliano.go.tz/frontend_api/api/pub/regions"

def store_regions(link):
    '''Gets json regions data from a url and writes it into a file'''
    # Fetch the JSON data
    with urllib.request.urlopen(link) as response:
        json_data = response.read()
    # Decode the JSON data
    data = json.loads(json_data)
    # Save JSON data to a file
    with open("regions.json", "w") as file:
        json.dump(data, file, indent=4)


# store_regions(url)

