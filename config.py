# config.py

# RS485-Konfiguration
RS485_PORT = 'COM3'  # Beispiel-Port, passe diesen an deine Umgebung an
BAUD_RATE = 19200  # Baudrate für RS485

# Datei-Pfade für die Ausgabedateien
TIME_FILE = "time.txt"
GOALS_HOME_FILE = "goals_home.txt"
GOALS_GUEST_FILE = "goals_guest.txt"
FOULS_HOME_FILE = "fouls_home.txt"
FOULS_GUEST_FILE = "fouls_guest.txt"

# Regex Patterns
TIME_PATTERN = r'(\d{4})\?\?RS'
GOALS_HOME_PATTERN = r'HG(\d{2})'  # Beispielpattern für Heimtore
GOALS_GUEST_PATTERN = r'GG(\d{2})'  # Beispielpattern für Gasttore
FOULS_HOME_PATTERN = r'HTF(\d{2})'  # Beispielpattern für Heim-Teamfouls
FOULS_GUEST_PATTERN = r'GTF(\d{2})'  # Beispielpattern für Gast-Teamfouls
