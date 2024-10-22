from config import TIME_FILE, GOALS_HOME_FILE, GOALS_GUEST_FILE, FOULS_HOME_FILE, FOULS_GUEST_FILE


class FileWriter:
    def __init__(self):
        # Datei-Pfade werden aus der Konfiguration geladen
        self.time_file = TIME_FILE
        self.goals_home_file = GOALS_HOME_FILE
        self.goals_guest_file = GOALS_GUEST_FILE
        self.fouls_home_file = FOULS_HOME_FILE
        self.fouls_guest_file = FOULS_GUEST_FILE

    def write_time(self, time):
        with open(self.time_file, 'w') as f:
            f.write(time)

    def write_goals_home(self, goals):
        with open(self.goals_home_file, 'w') as f:
            f.write(goals)

    def write_goals_guest(self, goals):
        with open(self.goals_guest_file, 'w') as f:
            f.write(goals)

    def write_fouls_home(self, fouls):
        with open(self.fouls_home_file, 'w') as f:
            f.write(fouls)

    def write_fouls_guest(self, fouls):
        with open(self.fouls_guest_file, 'w') as f:
            f.write(fouls)
