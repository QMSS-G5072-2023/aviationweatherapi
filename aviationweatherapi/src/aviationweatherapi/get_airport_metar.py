import requests

def get_airport_metar(airport_code):
    """
    Fetches METAR information for a given airport from the AviationWeather Data API.

    Args:
    airport_code (str): The ICAO code of the airport for which METAR information is requested.

    Returns:
    str: METAR information as a text string if the request is successful.
         Error message with status code if the request fails.
    
    Example:
    airport_metar = get_airport_metar('KJFK')
    print(airport_metar)
    """
    
    url = f'https://aviationweather.gov/api/data/metar?ids={airport_code}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return f'Error: {response.status_code}'