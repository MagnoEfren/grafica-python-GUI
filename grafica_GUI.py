# -*- coding: utf-8 -*-
"""Created  2021
@author: Magno Efren
https://www.youtube.com/c/MagnoEfren
"""
import serial,time,collections
import matplotlib.pyplot as plt
import matplotlib.animation as animacion
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from threading import Thread
from tkinter import Tk, Frame, StringVar, Label,Button,Entry


isReceiving= False 
isRun = True 
datos = 0.0
muestraD = 100
data = collections.deque([0]*muestraD, maxlen=muestraD)
xmin = 0
xmax = muestraD
ymin = -5
ymax = 5 

#"/dev/ttyUSBB"

try:
    arduino = serial.Serial("COM6", 9600 , timeout=1)
          
except:
    print("Error de coneccion con el puerto")


def Iniciar():
    global datos
    global isReceiving
    global isRun
    isReceiving = True
    isRun = True
   
    thread.start() 
    anim = animacion.FuncAnimation(fig, plotData,  fargs=(muestraD,lines),interval = 100, blit = False )
    plt.show()
    

def DatosA():
    time.sleep(1)
    arduino.reset_input_buffer()

    while (isRun):
        global isReceive
        global datos 
        datos = float(arduino.readline().decode('utf-8'))
        isReceive = True

def plotData(self,muestraD,lines):
    data.append(datos)
    lines.set_data(range(muestraD), data)

    labelx.set("VOL:" + str(datos)) 

thread = Thread(target = DatosA) 
 
def Salir():
    global isRun
    isRun = False 
    thread.join()
    arduino.close()
    time.sleep(1)
    raiz.destroy()
    raiz.quit()
    print("proceso finalizado")


def Terminar():
  
    global isRun
    global isReceiving 
    isRun = False 
    isReceiving = False

    time.sleep(0.5)
    thread.join(timeout=0.3)
    arduino.close()
    datos=00.0

# , figsize=(6, 5)   tamaño / , dpi=75  zoom / plt.cla()  borra  nombres x e y /

fig = plt.figure(facecolor="0.55",figsize=(6, 4), clear=True, dpi=100)
ax = plt.axes(xlim=(xmin,xmax),ylim=(ymin,ymax))
plt.title("Grafica - 0 - 5 Voltios",color='red',size=16, family="Tahoma")
ax.set_xlabel("Muestras")
ax.set_ylabel("Señal")

lines = ax.plot([] ,[], 'r')[0]

def Limpiar():
    fig.clf()


raiz = Tk()
raiz.protocol("WM_DELATE_WINDOW",Salir)
raiz.config(bg = "black")
raiz.title("  \t\t\t\t GRAFICA SEÑAL ANALOGICA")
raiz.geometry("738x402")
raiz.resizable(1,1)

lienzo = FigureCanvasTkAgg(fig, master = raiz )
lienzo._tkcanvas.grid(row = 0,column = 0, padx = 1,pady = 1)

frame = Frame(raiz, width = 130,height = 402, bg = "#7003FC")
frame.grid(row = 0,column = 1, padx = 1,pady = 2)
frame.grid_propagate(False)
frame.config(relief = "sunken")
frame.config(cursor = "heart")

labelx = StringVar(raiz, "VOL: 0.00")

label = Label(frame,textvariable = labelx, bg= "#5CFE05",fg="black", font="Helvetica 13 bold",width=11 ,justify="center")
label.pack()
label.grid(row=0,column=0, padx=5,ipady=8, pady=10)

Iniciar = Button(frame,command= Iniciar, text= "Iniciar ",bg="blue",fg="white", font="Helvetica 14 bold",width=9,justify="center")
Iniciar.pack
Iniciar.grid(row=1,column=0, padx=5,pady=5)

terminar = Button(frame,command= Terminar, text= "Terminar",bg="blue",fg="white", font="Helvetica 14 bold",width=9)
terminar.pack
terminar.grid(row=2,column=0, padx=5,pady=5)

limpiar = Button(frame,command= Limpiar, text= "Limpiar ",bg="blue",fg="white", font="Helvetica 14 bold",width=9,justify="center")
limpiar.pack
limpiar.grid(row=3,column=0, padx=5,pady=5)

salir = Button(frame,command= Salir, width=9 ,text= "SALIR",bg="red", font="Helvetica 14 bold",justify="center")
salir.pack
salir.grid(row=4,column=0, padx=5,pady=125)

raiz.mainloop()

