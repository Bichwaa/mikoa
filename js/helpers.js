/**
 * Get a list of all districts in a district
 * @param {string} regionName The name of the region whose districts are to be retrieved
 * @param {object} districtsData A JSON object that contains `data` attribute, an array of districs
 * @returns {Array<object>} An array of all districts in the region `regionName`
 */
function getDistricts(regionName = 'ARUSHA', districtsData = { data: []}) {
    const districts = districtsData.data.filter(district => district.parent.name.toLowerCase() === regionName.toLowerCase());

    return districts;
}

/**
 * Get a list of all wards in a district
 * @param {string} districtName The name of the district whose wards are to be retrieved
 * @param {object} wardsData A JSON object that contains `data` attribute, an array of wards
 * @returns {Array<object>} An array of all wards in the district `districtname`
 */
function getWards(districtName = 'ARUMERU', wardsData = {data: []}) {
    const wards = wardsData.data.filter(ward => ward.parent.name.toLowerCase() === districtName.toLowerCase());

    return wards;
}
