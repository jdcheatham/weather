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
			print (ct[4:10],',',ct[20:24],',',ct[11:19],',',data)
			
			outfile=open('weather','a')
			outfile.write(ct[4:10])
			outfile.write(" ")
			outfile.write(ct[20:24])
			outfile.write(",")
			outfile.write(ct[11:19])
			outfile.write(",")
			outfile.write(str(data))
			outfile.write("\n")
			outfile.close()

if __name__ == "__main__":
    main()
