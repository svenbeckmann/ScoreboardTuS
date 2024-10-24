import re
from config import TIME_PATTERN, GOALS_HOME_PATTERN, GOALS_GUEST_PATTERN, FOULS_HOME_PATTERN, FOULS_GUEST_PATTERN


class DataExtractor:
    def __init__(self):
        self.time_pattern = re.compile(TIME_PATTERN)
        self.goals_home_pattern = re.compile(GOALS_HOME_PATTERN)
        self.goals_guest_pattern = re.compile(GOALS_GUEST_PATTERN)
        self.fouls_home_pattern = re.compile(FOULS_HOME_PATTERN)
        self.fouls_guest_pattern = re.compile(FOULS_GUEST_PATTERN)

    def extract_time(self, data: str) -> str or None:
        """Extrahiert die Zeit aus dem gegebenen Datenstring."""
        match = self.time_pattern.search(data)
        if match:
            minutes = match.group(1)[:2]
            seconds = match.group(1)[2:]
            return f"{minutes}:{seconds}"
        return "00:00"  # Standardwert, wenn keine Übereinstimmung gefunden wird

    def extract_goals_home(self, data: str) -> str or None:
        """Extrahiert die Tore der Heimmannschaft aus dem gegebenen Datenstring."""
        match = self.goals_home_pattern.search(data)
        if match:
            return match.group(1)
        return "0"  # Standardwert

    def extract_goals_guest(self, data: str) -> str or None:
        """Extrahiert die Tore der Gastmannschaft aus dem gegebenen Datenstring."""
        match = self.goals_guest_pattern.search(data)
        if match:
            return match.group(1)
        return "0"  # Standardwert

    def extract_fouls_home(self, data: str) -> str or None:
        """Extrahiert die Teamfouls der Heimmannschaft aus dem gegebenen Datenstring."""
        match = self.fouls_home_pattern.search(data)
        if match:
            return match.group(1)
        return "0"  # Standardwert

    def extract_fouls_guest(self, data: str) -> str or None:
        """Extrahiert die Teamfouls der Gastmannschaft aus dem gegebenen Datenstring."""
        match = self.fouls_guest_pattern.search(data)
        if match:
            return match.group(1)
        return "0"  # Standardwert
