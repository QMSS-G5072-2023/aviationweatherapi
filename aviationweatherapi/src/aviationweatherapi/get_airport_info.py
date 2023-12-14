import requests

def get_airport_info(airport_code):
    
    """
    Fetches airport information from the AviationWeather Data API.

    Args:
    airport_code (str): The IATA/FAA code of the airport for which information is requested.
    Search single airport by enter the IATA/FAA code of the airport.
    Search multiple airports by enter a list of ICAO Ids separated by commas or spaces (KLAX,KSEA,KSNA).
    Search all airports in a certain state by enter a 2 letter state abbreviation preceded by a @ (@NY).

    Returns:
    str: Airport information as a text string if the request is successful.
         Error message with status code if the request fails.
         
    Example:
    airport_data = get_airport_info('KJFK')
    print(airport_data)
    """
    
    url = f'https://aviationweather.gov/api/data/airport?ids={airport_code}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return f'Error: {response.status_code}'