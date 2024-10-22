import serial


def read_from_rs485(port='COM3', baudrate=19200):
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        while True:
            if ser.in_waiting > 0:
                data = ser.readline().decode('ascii').strip()
                yield data
    except serial.SerialException as e:
        print(f"Error reading from RS485: {e}")
    finally:
        ser.close()
