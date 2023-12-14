def help_me():
    """
    Displays help information for the available functions.
    
    Example: 
    help_me()
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

help_me()
