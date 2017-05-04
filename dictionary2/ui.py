from tkinter import *
from tkinter import filedialog
from fh import readwrite
from threading import Thread

class Mythread(Thread):
    
    def __init__(self, tname, file_path, isDict, isSynonyms, l1):
        Thread.__init__(self, name=tname)
        self.file_path=file_path
        self.label=l1
        self.isDict=isDict
        self.isSynonyms=isSynonyms
        
    def run(self):
        print('Thread started', self.getName())  
        print(self.file_path)      
        if(readwrite(self.file_path, self.isDict, self.isSynonyms)>0):
            self.label.config(text='Done!')
            
def perform(isDict, isSynonyms):
    print('here')
    global file_path    
    global l1
    
    if(len(file_path)==0):
        l1.config(text='Select input file')
        return
    
    if(isDict or isSynonyms):
        l1.config(text='Running...')
        t2 = Mythread('T2', file_path, isDict, isSynonyms, l1)
        t2.start()
    else:
        l1.config(text='Select an option first')    

def choosefile():
    global file_path
    file_path = filedialog.askopenfilename()
    print('file_path=' +file_path)
    global l1
    l1.config(text='Input Selected')
    #l1.grid(row=5)

def checkbutton1():
    #print('here')
    global dropMenu1

    if(v1.get()==1):        
        dropMenu1.grid()
        #dropMenu1.pack()
    else:
        dropMenu1.grid_remove()
    
file_path=''    
root = Tk()
dropVar=StringVar()
optionList = ["Need examples","Don't need examples"]
dropVar.set('Need examples')
dropMenu1 = OptionMenu(root, dropVar,   *optionList)

dropMenu1.grid(row=2, column=2)
dropMenu1.grid_remove()
l = Label(root, text="Hello!")
l.grid(row=0)
b = Button(text="Choose Input", command=choosefile)
b.grid(row=1, sticky=E)

v1=IntVar()
v2=IntVar()

#l2 = Label(root, text="Dictionary")
#l3 = Label(root, text="Synonyms")

c1 = Checkbutton(root, text='Dictionary', variable = v1, command=checkbutton1)
c2 = Checkbutton(root, text='Synonyms', variable = v2)
c1.grid(row=2)
c2.grid(row=3)
Button(root,text='Go!',command=lambda:perform(v1.get(), v2.get())).grid(row=4)
Button(root, text='Quit', command=root.quit).grid(row=6)
l1 = Label(root, text='')
l1.grid(row=5)


root.mainloop()