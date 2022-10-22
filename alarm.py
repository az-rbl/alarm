from tkinter import *
from threading import *

root = Tk()
def work():
    pass

def  threading():
    t1=Thread(target=work, daemon=True)
    t1.start()

Button(root, text="click me", command=threading).pack()

root.mainloop()