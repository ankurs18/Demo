import pyautogui
from tkinter import *
from threading import Thread, Event
import time

class Mythread(Thread):
    
    def __init__(self, tname):
        Thread.__init__(self, name=tname)
        #self._stop = Event()
        
    def run(self):
        print('Thread started', self.getName())        
        global flag
        flag = not flag
        while(True):
            while(flag):
                pyautogui.keyDown('s')  
                time.sleep(1)       
    
def start():
    global t2
    global flag
    global counter
    counter+=1
    if(counter==1):    
        t2.start()
    else:
        flag=True

def exit():
    global root
    stop()
    root.destroy()

def stop():
    global flag
    flag=False
    print('here')
    
if __name__ == "__main__":    
    root=Tk()
    flag = False
    t2 = Mythread('T2')
    counter=0
    startbtn = Button(root,text='Start', fg = 'green', command = start)
    startbtn.pack()
    stopbtn = Button(root,text='Stop', fg = 'red', command = stop)
    stopbtn.pack()
    exitbtn = Button(root,text='Exit', fg = 'black', command = exit)
    exitbtn.pack()
    root.protocol("WM_DELETE_WINDOW", exit)
    root.mainloop()

 #pyinstaller demoautogui.py -F -w   

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    