import requests

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