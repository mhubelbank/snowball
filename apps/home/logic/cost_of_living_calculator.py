import re
import requests
import pandas as pd

def get_cost_of_living(city: str, state: str, total_adults: int, working_adults: int, children: int) -> float:
    """This function uses the MIT Cost of Living calculator to find the expected cost of living (after taxes) based on family size

    Parameters
    ----------
    city : str
        The city that you are living in
    state : str
        The state you are living in
    total_adults : int
        The total number of adults (1 or 2)
    working_adults : int
        The number of adults who work (1 or 2)
    children : int
        The number of children (currently 3 max, can extrapolate higher I think(?))

    Returns
    -------
    float
        Estimated cost of living after taxes as a float
    """

    if children > 3:
        return "Too many children!"

    # URL to get the latitude and longitude of a city
    LAT_LONG_URL = f"https://geocode.maps.co/search?q={city},{state}"

    response = requests.get(url=LAT_LONG_URL)

    # URL to get the FIPs code of a particular latitude and longitude
    latitude = response.json()[0]["lat"]
    longitude = response.json()[0]["lon"]
    FIPS_URL = f"https://geo.fcc.gov/api/census/area?lat={latitude}&lon={longitude}&censusYear=2020&format=json"

    response2 = requests.get(FIPS_URL)

    fips_code = response2.json()["results"][0]["county_fips"]

    # URL to get the cost of living tables from MIT Cost of Living calculator based on the FIPs code
    MIT_URL = f"https://livingwage.mit.edu/counties/{fips_code}"

    tables = pd.read_html(MIT_URL)

    if total_adults == 1:
        # Cost of living will always be in the second table on the page
        result = re.sub('[^0-9]','', tables[1].iloc[7][children + 1])
        return float(result)

    else:
        # Cost of living will always be in the second table on the page
        result = re.sub('[^0-9]','', tables[1].iloc[7][working_adults * 4 + children + 1])
        return float(result)