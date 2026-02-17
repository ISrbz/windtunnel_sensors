import serial
import serial.tools.list_ports

import os
import threading

### functions to display scale values bellow the scales ###
def showval(label, v):
    label['text'] = str(v[:5])

def showvalentr(label, txt, v, sc):
    v = txt.get()
    label['text'] = str(v)
    sc.set(v)

btnindx = False
btnstates = ["Disconnected", "Connected"]
def connectbtnfunc(connectlbl, port, baud):
    thr = threading.Thread(target= connect(port, baud))
    thr.daemon = True
    thr.start()
    global btnindx
    btnindx = not btnindx
    connectlbl['text'] = btnstates[btnindx]

coms = []
def findports():
    coms.clear()
    for port in serial.tools.list_ports.comports():
        if port.vid:
            coms.append(port.device)
    print(coms)

def connect(port, baud):
    command = "python3 monitor.py -p "+port.get()+" -b "+str(baud.get())
    os.system(command)
    

def refresh(self):
    self.destroy()
    self.__init__()