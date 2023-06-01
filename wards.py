import urllib.request
import json

def transform_dict(dictionary):
    transformed_dict = {
        "id": dictionary["id"],
        "name": dictionary["name"],
        "postcode": dictionary["postcode"],
        "parent": {
            "id": dictionary["parent"]["parent"]["id"],
            "name": dictionary["parent"]["parent"]["name"],
            "postcode": dictionary["parent"]["parent"]["postcode"]
        }
    }
    return transformed_dict



def get_ward(ward_id):
    '''Gets json ward data for one ward ,when given a region id'''
    
    url = f"https://napa.mawasiliano.go.tz/frontend_api/api/pub/skip_councils/{ward_id}"
    # Fetch the JSON data
    with urllib.request.urlopen(url) as response:
        json_data = response.read()
    # Decode the JSON data
    data = json.loads(json_data)
    for i in range(len(data['data'])):
        data['data'][i] = transform_dict(data['data'][i]) #transform_dict strips unnecesary data from each member of the ward list
    return data




def store_wards_in_file(data):
    # Save JSON data to a file
    try:
        with open(f"wards.json", "w") as file:
            json.dump(data, file, indent=4)   
    except Exception as e:
        print("An error occured while saving ward to file:", str(e))



def append_ward_to_Store(ward):
    try:
        # Read the existing JSON file
        with open("wards.json", "r") as file:
            existing_data = json.load(file)
        # Modify the Python object (append new data to old)
        existing_data["data"] = [*existing_data["data"], *ward["data"]]
        print("current total======>",len(existing_data['data']), " wards")
        store_wards_in_file(existing_data)
        
    except json.decoder.JSONDecodeError as e:
        #if file empty inform & write new data to store
        print("Store empty, appending one ward:", str(e))
        store_wards_in_file(ward)
        
        
        
# populate all wards
with open("districts.json", "r") as file:
    existing_data = json.load(file)
for i in existing_data["data"]:
    append_ward_to_Store(get_ward(i['id']))

# store_wards_in_file(get_ward(72350))