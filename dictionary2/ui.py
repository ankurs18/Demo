import tkinter as tk
from tkinter import filedialog
from fh import readwrite
from threading import Thread

class Mythread(Thread):
    
    def __init__(self, tname,file_path, l1):
        Thread.__init__(self, name=tname)
        self.file_path=file_path
        self.label=l1
        
    def run(self):
        print('Thread started', self.getName())        
        if(readwrite(self.file_path)>0):
            self.label.config(text='Done!')
            
def perform():
    
    file_path = filedialog.askopenfilename()
    
    l1 = tk.Label(root, text="File loaded, Dictionary compiling..")
    l1.grid(row=2)
    t2 = Mythread('T2', file_path, l1)
    t2.start()
    
root = tk.Tk()
l = tk.Label(root, text="Hello!")
l.grid(row=0)
b = tk.Button(text="Choose Input", command=perform)
b.grid(row=1)

root.mainloop()