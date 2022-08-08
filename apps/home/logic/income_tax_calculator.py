import requests

def get_effective_income_tax_rate(money: int, city: str, state: str, married:bool=False, dependents:int=1) -> float:
    """This function takes in tax-relevant parameters and returns the effective tax rate

    Parameters
    ----------
    money : int
        This is the income that will be taxed at a regular income tax rate. 
    city : str
        The city you are living in
    state : str
        The state you are living in
    married : bool, optional
        Whether you are married or not, by default False
    dependents : int, optional
        The number of dependents that you/your partner support (this typically doesn't matter, depends on the state), by default 1

    Returns
    -------
    float
        The effective tax rate based on the arguments
    """

    # This is the URL that the smartasset income tax calculator references for its API
    URL = f"https://smartasset.com/taxes/income-taxes?render=json&ud-current-location=CITY%7C{city}%7C{state}&ud-it-household-income={money}&ud-married={married}&ud-it-personal-exemptions={dependents}"

    # Headers so the request doesn't use the cached information in browser
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36',
    'cache-control': 'private, max-age=0, no-cache'
    }

    response = requests.get(URL, headers)

    # This means that the user entered a location that the website doesn't think exists
    if "invalid" in response.text:
        print("Invalid location")
        return 0

    return response.json()["page_data"]["2021"]["totalEffectiveTaxRate"] / 100