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
    
def average_elevation_by_state(state_code):
    """
    Fetches airport information for a given state and calculates the average elevation.

    Args:
    state_code (str): The state code for which average airport elevation is requested.
    The state_code needed to add within ''

    Returns:
    float: Average elevation of airports in the specified state.
           Returns None if there are no airports or in case of an error.
           
    Example:
    average_elevation = average_elevation_by_state('NY')
    print(average_elevation)
    
    """
    url = f'https://aviationweather.gov/api/data/airport?ids=@{state_code}'
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.text
    elevations = []

    for line in data.split('\n'):
        if 'Elevation' in line:
            try:
                elevation = float(line.split(':')[1].strip())
                elevations.append(elevation)
            except ValueError:
                continue

    if elevations:
        return sum(elevations) / len(elevations)
    else:
        return None
    
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
    
def easy_metar(metar):
    
    """
    Parses a METAR weather report string into a more readable format.
    
    !!!This function will not translate REMARK!!!
    
    Args:
    metar (str): The METAR string to be parsed.

    Returns:
    str: A more readable weather report.
    
    Example:
    metar_str = "KJFK 140651Z 31012G19KT 10SM FEW250 01/M08 A3060 RMK AO2 SLP361 T00111083"
    print(parse_metar(metar_str))
    
    """
    
    parts = metar.split()
    readable_report = []

    # Time
    date_time = f"Date and time of the report: {parts[1][0:2]}th of the month at {parts[1][2:4]}:{parts[1][4:6]} Zulu (UTC) time."
    readable_report.append(date_time)

    # Wind
    wind = f"Wind: From the {convert_wind_direction(parts[2][:3])} ({parts[2][:3]} degrees) at {parts[2][3:5]} knots."
    readable_report.append(wind)

    # Visibility
    visibility = f"Visibility: {parts[3]} statute miles."
    readable_report.append(visibility)

    # Clouds 
    cloud_index = 4
    while parts[cloud_index][:3] in ["FEW", "SCT", "BKN", "OVC", "CLR", "SKC"]:
        clouds = f"Clouds: {parse_clouds(parts[cloud_index])}"
        readable_report.append(clouds)
        cloud_index += 1

    # Temperature/Dewpoint
    temp_dew = f"Temperature: {parts[cloud_index].split('/')[0]}°C, Dewpoint: {parts[cloud_index].split('/')[1]}°C."
    readable_report.append(temp_dew)

    # Altimeter
    altimeter = f"Altimeter: {parts[cloud_index + 1][1:]} inches of Mercury (Hg)."
    readable_report.append(altimeter)

    # Remarks - NONE
    if len(parts) > cloud_index + 2:
        remarks = f"Remarks: {parse_remarks(' '.join(parts[cloud_index + 2:]))}"
        readable_report.append(remarks)

    return '\n'.join(readable_report)

def convert_wind_direction(direction):
    pass

def parse_clouds(cloud_info):
    cloud_codes = {
        "FEW": "Few clouds",
        "SCT": "Scattered clouds",
        "BKN": "Broken clouds",
        "OVC": "Overcast"
    }

    cloud_type = cloud_codes.get(cloud_info[:3], "Unknown cloud type")
    cloud_height = int(cloud_info[3:]) * 100  # Height is in hundreds of feet
    return f"{cloud_type} at {cloud_height} feet"

def parse_remarks(remarks):
    pass

def help_():
    """
    Displays help information for the available functions.
    
    Example: 
    help_()
    """
    help_text = """
    Available Functions:

    1. get_airport_info(airport_code):
       - Description: Fetches detailed information for a given airport using its ICAO code.
       - Input: airport_code (str) - ICAO code of the airport.
       - Search single airport by enter the IATA/FAA code of the airport.
       - Search multiple airports by enter a list of ICAO Ids separated by commas or spaces (KLAX,KSEA,KSNA).
       - Search all airports in a certain state by enter a 2 letter state abbreviation preceded by a @ (@NY).
       - Output: Airport information as a text string.
       
    2. get_average_elevation_by_state(state_code):
       - Description: Calculates the average elevation of airports in a specific state.
       - Input: state_code (str) - Code of the state.
       - Output: Average elevation of airports in the state as a float.

    3. get_airport_metar(airport_code):
       - Description: Fetches METAR weather report for a given airport using its ICAO code.
       - Input: airport_code (str) - ICAO code of the airport.
       - Output: METAR information as a text string.
 
    4. easy_metar(metar):
       - Description: Parses a METAR weather report string into a more readable format.
                      !!!This function will not translate REMARK!!!
       - Input: airport metar (str), can be directly parses from get_airport_metar function.
       - Output: METAR information as a text string.
            
    """
    print(help_text)
