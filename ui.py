import tkinter as tk
from data_extractor import DataExtractor
from file_writer import FileWriter


class ScoreboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scoreboard TuS")
        self.extractor = DataExtractor()
        self.writer = FileWriter()

        # Labels für Anzeige
        self.time_label = tk.Label(
            root, text="Time: 00:00", font=("Helvetica", 24))
        self.time_label.pack()

        self.goals_home_label = tk.Label(
            root, text="Heim Tore: 0", font=("Helvetica", 18))
        self.goals_home_label.pack()

        self.goals_guest_label = tk.Label(
            root, text="Gast Tore: 0", font=("Helvetica", 18))
        self.goals_guest_label.pack()

        self.fouls_home_label = tk.Label(
            root, text="Heim Teamfouls: 0", font=("Helvetica", 18))
        self.fouls_home_label.pack()

        self.fouls_guest_label = tk.Label(
            root, text="Gast Teamfouls: 0", font=("Helvetica", 18))
        self.fouls_guest_label.pack()

    def update_labels(self, data):
        time = self.extractor.extract_time(data)
        if time:
            self.time_label.config(text=f"Time: {time}")
            self.writer.write_time(time)

        goals_home = self.extractor.extract_goals_home(data)
        if goals_home:
            self.goals_home_label.config(text=f"Heim Tore: {goals_home}")
            self.writer.write_goals_home(goals_home)

        goals_guest = self.extractor.extract_goals_guest(data)
        if goals_guest:
            self.goals_guest_label.config(text=f"Gast Tore: {goals_guest}")
            self.writer.write_goals_guest(goals_guest)

        fouls_home = self.extractor.extract_fouls_home(data)
        if fouls_home:
            self.fouls_home_label.config(text=f"Heim Teamfouls: {fouls_home}")
            self.writer.write_fouls_home(fouls_home)

        fouls_guest = self.extractor.extract_fouls_guest(data)
        if fouls_guest:
            self.fouls_guest_label.config(
                text=f"Gast Teamfouls: {fouls_guest}")
            self.writer.write_fouls_guest(fouls_guest)
