from tkinter import *
from tkinter import ttk

from func import *

### sensor otputs ###
# gotta un-hardcode recieve trough Serial from arduino
time = 0
temp = 293.15
p = 98985.53
v = 2
aoa = 0


### define frames like ###
#     _______ 
#    |_______|
#    |   |   |
#    |___|___|

root = Tk()
titlefrm = ttk.Frame(root, padding=10)
titlefrm.grid(row=0, columnspan=6, rowspan=2)

frm = ttk.Frame(root, padding=0)
frm.grid(row=1, column=0, rowspan=5, columnspan=2)
dynam = ttk.Frame(frm, padding=10)
dynam.grid(row=0, column=0)
stat = ttk.Frame(frm, padding=10)
stat.grid(row=0, column=1)

frm2 = ttk.Frame(root, padding=10)
frm2.grid(row=4, column=2, rowspan=2, columnspan=4)

### variables for the scales and inputs ###
v1 = DoubleVar()
v2 = DoubleVar()
txt1 = DoubleVar()
txt2 = DoubleVar()
com = StringVar()
baud = IntVar(value=9600)

### text above all ###
# ...here are supposed to be settings for serial communication with the arduino (baudrate | port | connect/disconnect)
findports()
comlbl = ttk.Label(titlefrm, text="Port:", font=("Arial", 12))
comentr = ttk.Combobox(titlefrm, textvariable=com, values=coms, font=("Arial", 12), width=10)
comentr.bind('<<ComboboxSelected>>', lambda _: findports())
#comentr.bind()
baudlbl = ttk.Label(titlefrm, text="Baudrate:", font=("Arial", 12))
baudentr = ttk.Entry(titlefrm, textvariable=baud, font=("Arial", 12), width=6)
connectlbl = ttk.Label(titlefrm, text="Disconnected", font=("Arial", 12), width=12)
connectbtn = ttk.Button(titlefrm, text="Connect/Disconnect", command=lambda lbl=connectlbl: connectbtnfunc(lbl, com, baud))  

### show sensor values ###
timelbl = ttk.Label(dynam, text=time, background="#fafafa", width=10, anchor=CENTER, font=("Arial", 12), relief='solid')
templbl = ttk.Label(dynam, text=temp, background="#fafafa", width=10, anchor=CENTER, font=("Arial", 12), relief='solid')
plbl = ttk.Label(dynam, text=p, background="#fafafa", width=10, anchor=CENTER, font=("Arial", 12), relief='solid')
vlbl = ttk.Label(dynam, text=v, background="#fafafa", width=10, anchor=CENTER, font=("Arial", 12), relief='solid')
aoalbl = ttk.Label(dynam, text=aoa, background="#fafafa" , width=10, anchor=CENTER, font=("Arial", 12), relief='solid')

### show value dimension, measurement unit ###
timelbllbl = ttk.Label(stat, text="t, s", anchor=W, font=("Arial", 12))
templbllbl = ttk.Label(stat, text="T, K", anchor=W, font=("Arial", 12))
plbllbl = ttk.Label(stat, text="P, Pa", anchor=W, font=("Arial", 12))
vlbllbl = ttk.Label(stat, text="v, m/s", anchor=W, font=("Arial", 12))
aoalbllbl = ttk.Label(stat, text="AOA, deg", anchor=W, font=("Arial", 12))

### scale values bellow the scales ###
scale1lbl = ttk.Label(frm2, text='0', anchor=CENTER, font=("Arial", 15))
scale2lbl = ttk.Label(frm2, text='0', font=("Arial", 15))

### scales ###
scale1 = ttk.Scale(frm2, variable=v1, from_=100, to=0, orient=VERTICAL, command=lambda x, lbl=scale1lbl: showval(lbl, x), length=200)
scale2 = ttk.Scale(frm2, variable=v2, from_=200, to=0, orient=VERTICAL, command=lambda x, lbl=scale2lbl: showval(lbl, x), length=200)

### inputs ###
scale1entr = ttk.Entry(frm2, textvariable=txt1, width=5, font=("Arial", 15))
scale1entr.bind("<Return>", lambda x, lbl=scale1lbl: showvalentr(lbl, txt1, v1, scale1))
scale2entr = ttk.Entry(frm2, textvariable=txt2, width=5, font=("Arial", 15))
scale2entr.bind("<Return>", lambda x, lbl=scale2lbl: showvalentr(lbl, txt2, v2, scale2))

### quit button ###
button = ttk.Button(frm2, text="Quit", command=root.destroy)

### position ###
comlbl.grid(column=0, row=0, padx=15)
comentr.grid(column=0, row=1, pady=10, padx=15)
baudlbl.grid(column=1, row=0, padx=15)
baudentr.grid(column=1, row=1, pady=10, padx=15)
connectlbl.grid(column=2, row=0, padx=15)
connectbtn.grid(column=2, row=1, pady=10, padx=15)

timelbl.grid(column = 0, row = 0, pady=15, padx=10)
timelbllbl.grid(column = 1, row = 0, pady=15, padx=10)
templbl.grid(column = 0, row = 1, pady=15, padx=10)
templbllbl.grid(column = 1, row = 1, pady=15, padx=10)
plbl.grid(column = 0, row = 2, pady=15, padx=10)
plbllbl.grid(column = 1, row = 2, pady=15, padx=10)
vlbl.grid(column = 0, row = 3, pady=15, padx=10)
vlbllbl.grid(column = 1, row = 3, pady=15, padx=10)
aoalbl.grid(column = 0, row = 4, pady=15, padx=10)
aoalbllbl.grid(column = 1, row = 4, pady=15, padx=10)

scale1.grid(column=3, row=1, rowspan=3, padx=20, pady=15)
scale1lbl.grid(column=3, row=4, pady=0, padx=10)
scale1entr.grid(column=3, row=5, pady=10, padx=10)
scale2.grid(column=5, row=1, rowspan=3, padx=20, pady=15)
scale2lbl.grid(column=5, row=4, pady=0, padx=10)
scale2entr.grid(column=5, row=5, pady=10, padx=10)

button.grid(column=2, row=6, columnspan=2, pady=15, padx=10)

dynam.after(1000, lambda x=dynam: refresh(x))

### start ###
root.mainloop()