import serial
ser = serial.Serial()
ser.baudrate = 19200
ser.port = '/dev/tty.usbmodem55860048461'
ser.timeout = 1
ser.open()


#ser.write(serialcmd.encode('0x5A0x7E0x810x080x010x310xBB0x810xA5'))
#command = '0x5A0x7E0x810x080x010x310xBB0x810xA5'
#ser.write(command)

#print(ser.name)         
#ser.readline()
print (ser.readline())
ser.close() 