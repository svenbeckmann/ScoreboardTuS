import re

# Muster für die Spielzeit
TIME_PATTERN = r'(\d{4})\?\?RS'


def extract_time_data(line):
    match = re.search(TIME_PATTERN, line)
    if match:
        time_str = match.group(1)
        minutes = time_str[:2]
        seconds = time_str[2:]
        return minutes, seconds
    return None, None
