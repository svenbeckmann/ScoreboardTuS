from config import TIME_FILE, GOALS_HOME_FILE, GOALS_GUEST_FILE, FOULS_HOME_FILE, FOULS_GUEST_FILE


class FileWriter:
    def __init__(self):
        # Datei-Pfade werden aus der Konfiguration geladen
        self.time_file = TIME_FILE
        self.goals_home_file = GOALS_HOME_FILE
        self.goals_guest_file = GOALS_GUEST_FILE
        self.fouls_home_file = FOULS_HOME_FILE
        self.fouls_guest_file = FOULS_GUEST_FILE

    def write_to_file(self, file_path, data):
        try:
            with open(file_path, 'w') as f:
                f.write(data)
        except Exception as e:
            print(f"Error writing to {file_path}: {e}")

    def write_time(self, time):
        self.write_to_file(self.time_file, time)

    def write_goals_home(self, goals):
        self.write_to_file(self.goals_home_file, goals)

    def write_goals_guest(self, goals):
        self.write_to_file(self.goals_guest_file, goals)

    def write_fouls_home(self, fouls):
        self.write_to_file(self.fouls_home_file, fouls)

    def write_fouls_guest(self, fouls):
        self.write_to_file(self.fouls_guest_file, fouls)
