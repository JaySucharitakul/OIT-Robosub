# 
# This program will establish a UART communication line across COM3 to the Arduino
# https://pyserial.readthedocs.io/en/latest/pyserial_api.html
# https://pyserial.readthedocs.io/en/latest/shortintro.html#opening-serial-ports

import serial

with serial.Serial('/dev/ttyUSB0', 9600, timeout = 1) as port: # Open Serial port
	port.write(b'<11,45,0,1>')
	line = port.readline()  # read '\n' terminated line

print(line)
port.close()