# config.py

import platform

# RS485-Konfiguration
if platform.system() == 'Windows':
    RS485_PORT = 'COM3'  # Beispiel für Windows
elif platform.system() == 'Darwin':  # macOS
    RS485_PORT = '/dev/tty.usbmodem55860048461'
else:
    RS485_PORT = '/dev/ttyUSB0'  # Beispiel für Linux

BAUD_RATE = 19200  # Baudrate für RS485

# Datei-Pfade für die Ausgabedateien
TIME_FILE = "time.txt"
GOALS_HOME_FILE = "goals_home.txt"
GOALS_GUEST_FILE = "goals_guest.txt"
FOULS_HOME_FILE = "fouls_home.txt"
FOULS_GUEST_FILE = "fouls_guest.txt"

# Regex Patterns
TIME_PATTERN = r'(\d{4})\?\?RS'
GOALS_HOME_PATTERN = r'\?\?RD&! (\d+)$'  # Beispielpattern für Heimtore
GOALS_GUEST_PATTERN = r'\?\?RD&\) (\d+)$'  # Beispielpattern für Gasttore
FOULS_HOME_PATTERN = r'\?\?RD# (\d+)$'  # Beispielpattern für Heim-Teamfouls
FOULS_GUEST_PATTERN = r'\?\?RD#\$ (\d+)$'  # Beispielpattern für Gast-Teamfouls
