import re
import requests
import pandas as pd

# This function uses the MIT Cost of Living calculator to find the expected cost of living based on family size
# Arguments:
#   city            - The city that you are living in
#   state           - The state you are living in
#   total_adults    - The total number of adults (1 or 2)
#   working_adults  - The number of adults who work (1 or 2)
#   children        - The number of children (currently 3 max, can extrapolate higher I think(?))
# Returns:
#   Estimated cost of living after taxes as a float
def get_cost_of_living(city, state, total_adults, working_adults, children):

    if children > 3:
        return "Too many children!"

    # URL to get the latitude and longitude of a city
    LATLONGURL = "http://api.openweathermap.org/geo/1.0/direct?q=" + city + "," + state + ",US&limit=1&appid=d375f2270b268435bedceb0d3bff9de6"

    response = requests.get(url=LATLONGURL)

    # URL to get the FIPs code of a particular latitude and longitude
    FIPSURL = "https://geo.fcc.gov/api/census/area?lat=" + str(response.json()[0]["lat"]) + "&lon=" + str(response.json()[0]["lon"]) + "&censusYear=2020&format=json"

    response2 = requests.get(FIPSURL)

    fips_code = response2.json()["results"][0]["county_fips"]

    # URL to get the cost of living tables from MIT Cost of Living calculator based on the FIPs code
    MITURL = "https://livingwage.mit.edu/counties/" + str(fips_code)

    tables = pd.read_html(MITURL)

    if total_adults == 1:
        # Cost of living will always be in the second table on the page
        result = re.sub('[^0-9]','', tables[1].iloc[7][children + 1])
        return float(result)

    else:
        # Cost of living will always be in the second table on the page
        result = re.sub('[^0-9]','', tables[1].iloc[7][working_adults * 4 + children + 1])
        return float(result)