""" Python code to read serial port
    J. Cheahtam
    using http://www.instructables.com/id/Arduino-Python-Communication-via-USB/"""
    
import serial
import time

arduino = serial.Serial('COM7',9600, timeout=.1)
def main():
       
	while True:
		data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
		ct = time.asctime( time.localtime(time.time()) )
		if data:
			print (ct,data)

if __name__ == "__main__":
    main()
