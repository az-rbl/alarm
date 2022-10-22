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
        self.running = True
        self.lock = threading.Lock()
        self.cv = threading.Condition(lock=self.lock)
    
    def modify_file(self):
        self.file=filedialog.askopenfilename()
        print(self.file)
        if self.file != '':
            with self.cv:
                self.cv.notify_all()
    
    def modify_running(self):
        self.running = not self.running
    
    def read_file(self):
        self.cv.acquire()
        while self.file == '':
            self.cv.wait()
        self.cv.release()
        return self.file


def buzz(monitor:monitor):
    while(monitor.running==True):
        objeto = pyautogui.locateOnScreen(monitor.read_file())
        print("1")
        if(objeto !=None ): 
            print("objeto encontrado")
            winsound.Beep(freq, duration)
        time.sleep(2)
        global stop_threads
        if stop_threads:
            break

def gui(monitor:monitor):
    root=tkinter.Tk()
    root.title("Alarma")
    button1 =tkinter.Button(root, text = 'parar', width="25", command=monitor.modify_running)
    button1.pack()
    button2 =tkinter.Button(root, text ='Examinar', command=monitor.modify_file )
    button2.pack()
    root.mainloop()
    
    
def file(file,stop):
    file=filedialog.askopenfile()

def fin(r,x):
    r.destroy
    x.join

mo = monitor()
stop_threads = False
x = threading.Thread(target=buzz, args =[mo], daemon=True)
x.start()
window = threading.Thread(target=gui, args=[mo] ,daemon=True)
window.start()
#stop_threads =True
x.join()
sys.exit()




