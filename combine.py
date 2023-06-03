import json
from utils.helpers import get_districts, get_wards

def main():
    combined_data = {
        'regions': [],
    }
    # open and read the json files
    with open("regions.json", "r") as regions_file, open("districts.json", "r") as districts_file, open("wards.json", "r") as wards_file:
        regions_data = json.load(regions_file)
        districts_data = json.load(districts_file)
        wards_data = json.load(wards_file)

        for region in regions_data['data']:
            region_name = region['name']
            districts = get_districts(region_name, districts_data)
            # get wards for each district
            for district in districts:
                district_name = district['name']
                wards = get_wards(district_name, wards_data)
                district['wards'] = wards

            region['districts'] = districts
            combined_data['regions'].append(region)


    # write to combined_data.json
    with open("combined_data.json", "w") as combined_data_file:
        json.dump(combined_data, combined_data_file, indent=4)

    return combined_data

main()