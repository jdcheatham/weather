""" Python code to read serial port
    J. Cheahtam
    using http://www.instructables.com/id/Arduino-Python-Communication-via-USB/"""
    
import serial
import time

def main():
arduino = serial.Serial('COM1',9600, timeout=.1)
while True:
	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
	if data:
		print data

if __name__ = "__main__":
    main()