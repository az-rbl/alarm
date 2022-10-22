from os import system
from tkinter import filedialog
import pyautogui
import time
import winsound
import tkinter
import threading
import sys

duration = 1000  # milliseconds
freq = 440  # Hz

class monitor():
    def __init__(self):
        self.file =''
        self.stopped = False
    
    def modify_file():
        pass

def buzz(file,stop):
    while(True):
        time.sleep(2)
        objeto = pyautogui.locateOnScreen(r"C:\Users\lnvo\Documents\so\alarm\objeto.png")
        print("1")
        if(objeto !=None ): 
            print("objeto encontrado")
            winsound.Beep(freq, duration)
        global stop_threads
        if stop_threads:
            break
def gui(file,stop):
    f=''
    root=tkinter.Tk()
    root.title("Alarma")
    button1 =tkinter.Button(root, text = 'parar', width="25", command=root.destroy)
    button1.pack()
    button2 =tkinter.Button(root, text ='Examinar', command=file )
    button2.pack()
    root.mainloop()
    
    
def file(file,stop):
    file=filedialog.askopenfile()

def fin(r,x):
    r.destroy
    x.join


stop_threads = False
x = threading.Thread(target=buzz, daemon=True)
x.start()
window = threading.Thread(target=gui,daemon=True)
window.start()
#stop_threads =True
x.join()
sys.exit()




