import serial
from config import RS485_PORT, BAUD_RATE


class RS485Reader:
    def __init__(self, port=RS485_PORT, baudrate=BAUD_RATE):
        try:
            # Verwende die konfigurierten Werte und öffne die serielle Verbindung
            self.ser = serial.Serial(port, baudrate, timeout=1)
            print(f"Connected to {port} at {baudrate} baud.")
        except serial.SerialException as e:
            print(f"Error opening serial port {port}: {e}")
            self.ser = None

    def read_data(self):
        if self.ser and self.ser.in_waiting > 0:
            try:
                data = self.ser.readline().decode('utf-8').strip()
                return data
            except Exception as e:
                print(f"Error reading data: {e}")
                return None
        return None
