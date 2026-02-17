import serial
import serial.tools.list_ports


for port in serial.tools.list_ports.comports():
    if port.vid:
        print(port.device)