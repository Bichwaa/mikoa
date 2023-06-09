def get_districts(region_name='ARUSHA', districts_data={'data': []}):
    print("Getting districts for region: " + region_name + "\n")
    districts = [district for district in districts_data['data'] if district['parent']['name'].lower() == region_name.lower()]
    return districts


def get_wards(district_name='ARUMERU', wards_data={'data': []}):
    print("Getting wards for district: " + district_name + "\n")
    wards = [ward for ward in wards_data['data'] if ward['parent']['name'].lower() == district_name.lower()]
    return wards

