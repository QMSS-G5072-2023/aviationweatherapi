import requests

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