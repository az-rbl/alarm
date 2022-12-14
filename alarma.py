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
        self.file =[]
        self.running = True
        self.lock = threading.Lock()
        self.cv = threading.Condition(lock=self.lock)
    
    def modify_file(self):
        self.lock.acquire()
        self.file.append(filedialog.askopenfilename(filetypes=[("Imagenes",".png .jpg")]))
        self.lock.release()
        print(self.file)
        if self.file != []:
            with self.cv:
                self.cv.notify_all()
    
    def modify_running(self):
        self.running = not self.running
    
    def read_file(self):
        self.cv.acquire()
        while self.file == []:
            self.cv.wait()
        self.cv.release()
        
        return self.file.pop()  


def buzz(monitor:monitor):
    while(True):
        ruta=monitor.read_file()
        buscando= True
        while(buscando==True):
            objeto = pyautogui.locateOnScreen(ruta)
            #print(objeto)
            print("1")
            if(objeto !=None ): 
                print("objeto encontrado")
                print(objeto)
                buscando=(False)
                winsound.Beep(freq, duration)
            
        #time.sleep(0.5)
        # global stop_threads
        # if stop_threads:
        #     break

def gui(monitor:monitor):
    root=tkinter.Tk()
    root.title("Alarma")
    button1 =tkinter.Button(root, text = 'parar', width="25", command=monitor.modify_running)
    button1.pack()
    button2 =tkinter.Button(root, text ='Examinar', command=monitor.modify_file )
    button2.pack()
    root.mainloop()
    

mo = monitor()

stop_threads = False
x = threading.Thread(target=buzz, args =[mo], daemon=True)
x.start()
window = threading.Thread(target=gui, args=[mo] )
window.start()
window2 = threading.Thread(target=gui, args=[mo] )
window2.start()
window3 = threading.Thread(target=gui, args=[mo] )
window3.start()
#stop_threads =True
x.join()
window.join()
sys.exit()