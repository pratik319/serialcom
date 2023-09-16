import serial
import time


def readserial(comport, baudrate, timestamp=False):

    ser = serial.Serial(comport, baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read
    
    while True:

        data = ser.readline().decode('latin-1').strip()

        if data and timestamp:
            timestamp = time.strftime('%H:%M:%S')
            print(f'{timestamp} > {data}')
        elif data:
            print(data)
            

readserial('COM3',9600, False)                          # COM port, Baudrate, Show timestamp