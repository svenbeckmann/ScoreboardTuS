import tkinter as tk
from data_extractor import extract_time_data
from file_writer import write_to_file
from rs485_reader import read_from_rs485
from config import TIME_FILE


def start_ui():
    root = tk.Tk()
    root.title("Scoreboard TuS")

    time_label = tk.Label(root, text="Spielzeit: 00:00",
                          font=("Helvetica", 24))
    time_label.pack(pady=20)

    def update_time():
        for line in read_from_rs485():
            minutes, seconds = extract_time_data(line)
            if minutes is not None and seconds is not None:
                time_str = f"{minutes}:{seconds}"
                time_label.config(text=f"Spielzeit: {time_str}")
                write_to_file(TIME_FILE, time_str)
            root.after(1000, update_time)  # Aktualisierung alle 1 Sekunde

    root.after(1000, update_time)
    root.mainloop()
