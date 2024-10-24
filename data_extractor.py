import re
from config import TIME_PATTERN, GOALS_HOME_PATTERN, GOALS_GUEST_PATTERN, FOULS_HOME_PATTERN, FOULS_GUEST_PATTERN


class DataExtractor:
    def __init__(self):
        # Regex-Muster für verschiedene Datenarten
        self.time_pattern = re.compile(TIME_PATTERN)
        self.goals_home_pattern = re.compile(GOALS_HOME_PATTERN)
        self.goals_guest_pattern = re.compile(GOALS_GUEST_PATTERN)
        self.fouls_home_pattern = re.compile(FOULS_HOME_PATTERN)
        self.fouls_guest_pattern = re.compile(FOULS_GUEST_PATTERN)

    def extract_time(self, data):
        match = self.time_pattern.search(data)
        if match:
            # Minuten (1 oder 2 Ziffern) und Sekunden (2 Ziffern)
            minutes = match.group(1).decode('utf-8')
            seconds = match.group(2).decode('utf-8')
            return f"{minutes}:{seconds}"
        return None

    def extract_goals_home(self, data):
        match = self.goals_home_pattern.search(data)
        if match:
            return match.group(1).decode('utf-8')  # Heimtore
        return None

    def extract_goals_guest(self, data):
        match = self.goals_guest_pattern.search(data)
        if match:
            return match.group(1).decode('utf-8')
        return None

    def extract_fouls_home(self, data):
        match = self.fouls_home_pattern.search(data)
        if match:
            return match.group(1).decode('utf-8')
        return None

    def extract_fouls_guest(self, data):
        match = self.fouls_guest_pattern.search(data)
        if match:
            return match.group(1).decode('utf-8')
        return None
