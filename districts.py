import urllib.request
import json

def transform_dict(dictionary):
    transformed_dict = {
        "id": dictionary["id"],
        "name": dictionary["name"],
        "postcode": dictionary["postcode"],
        "parent": {
            "id": dictionary["parent"]["id"],
            "name": dictionary["parent"]["name"],
            "postcode": dictionary["parent"]["postcode"]
        }
    }
    return transformed_dict



def get_district(region_id):
    '''Gets json district data for one district ,when given a region id'''
    
    url = f"https://napa.mawasiliano.go.tz/frontend_api/api/pub/districts/{region_id}"
    # Fetch the JSON data
    with urllib.request.urlopen(url) as response:
        json_data = response.read()
    # Decode the JSON data
    data = json.loads(json_data)
    for i in range(len(data['data'])):
        data['data'][i] = transform_dict(data['data'][i]) #transform_dict strips unnecesary data from each member of the district list
    return data




def store_districts_in_file(data):
    # Save JSON data to a file
    try:
        with open(f"districts.json", "w") as file:
            json.dump(data, file, indent=4)   
    except Exception as e:
        print("An error occured while saving district to file:", str(e))



def append_district_to_Store(district):
    try:
        # Read the existing JSON file
        with open("districts.json", "r") as file:
            existing_data = json.load(file)
        # Modify the Python object (append new data to old)
        existing_data["data"] = [*existing_data["data"], *district["data"]]
        print("current total======>",len(existing_data['data']), " Districts")
        store_districts_in_file(existing_data)
        
    except json.decoder.JSONDecodeError as e:
        #if file empty inform & write new data to store
        print("Store empty, appending one district:", str(e))
        store_districts_in_file(district)
        
        
        
# populate all districts
with open("regions.json", "r") as file:
    existing_data = json.load(file)
for i in existing_data["data"]:
    append_district_to_Store(get_district(i['id']))

# store_districts_in_file(get_district(70844))