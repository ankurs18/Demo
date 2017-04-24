from tkinter import *
#from lxml.html import submit_form

def show(val1, val2):
    print('Hello', val1+' '+val2)



root=Tk()

l1=Label(root, text='Enter your name')
l1.grid(row=0)

ent1= Entry(root)
ent1.grid(row=0, column =1)

l2=Label(root, text='Enter password')
ent2= Entry(root)
l2.grid(row=1)
ent2.grid(row=1, column =1)

v=IntVar()
l3= Label(root, text = 'Choose your Gender')
r1 = Radiobutton(root, text='Male', variable = v, value=1)
r2 = Radiobutton(root, text='Female', variable = v, value=2)
l3.grid(row=2)
r1.grid(row=2, column =0)
r2.grid(row=2, column =1)

v2=IntVar()
v3=IntVar()
l4= Label(root, text = 'Choose your Language')
c1 = Checkbutton(root, text='Java', variable = v2)
c2 = Checkbutton(root, text='Python', variable = v3)
l4.grid(row=3)
c1.grid(row=3, column =0)
c2.grid(row=3, column =1)


l5=Label(root, text = 'Education')
list1=Listbox(root, height = 3)
list1.insert(1, 'BE')
list1.insert(2, 'MBA')
list1.insert(3, 'BCA')

l5.grid(row = 4)
list1.grid(row=4, column = 1)

submit = Button(root,text='Submit', fg = 'red', command = lambda:show(ent1.get(), ent2.get()))
submit.grid(row = 5)

root.mainloop()