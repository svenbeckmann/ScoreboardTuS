from rs485_reader import RS485Reader
from ui import ScoreboardApp
import tkinter as tk


def main():
    root = tk.Tk()
    reader = RS485Reader()  # RS485-Port

    # Übergibt den Reader an die ScoreboardApp
    app = ScoreboardApp(root, reader)

    def update_data():
        data = reader.read_data()
        if data:
            app.update_labels(data)
        root.after(1000, update_data)  # Wiederhole alle 1 Sekunde

    update_data()
    root.mainloop()


if __name__ == "__main__":
    main()
