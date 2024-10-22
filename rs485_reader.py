import serial
from config import RS485_PORT, BAUD_RATE


class RS485Reader:
    def __init__(self, port=RS485_PORT, baudrate=BAUD_RATE):
        # Verwende die konfigurierten Werte
        self.ser = serial.Serial(port, baudrate, timeout=1)

    def read_data(self):
        if self.ser.in_waiting > 0:
            data = self.ser.readline().decode('utf-8').strip()
            return data
        return None
