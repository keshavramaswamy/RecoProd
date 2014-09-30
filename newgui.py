from Tkinter import *
import os
   
def recopro():

   text.insert(INSERT,"The optimal product is:\n\n")
   fp=open("reco.txt","r")
   for line in fp:
      text.insert(INSERT,line)
   text.insert(INSERT,"\n\nWe also recommend the following products:\n\n")   
   fp1=open("reco1.txt","r")
   for line in fp1:
      text.insert(INSERT,line)
   text.pack()
   
   
   

def fingraph():
   os.system('kmeans.png')
   
   
def open1():
   if var.get() == 1:
      os.system('op1.png')
      print 'a'
   elif var.get() == 2:
      os.system('op2.png')
      print 'b'
   elif var.get() == 3:
      os.system('op3.png')
      print 'c'

def tmp():
   global text
   text = Text(root2)

def camera1():
   clear1()
   if var.get() == 1:
      fp=open("1_camera.txt","r")
   elif var.get() == 2:
      fp=open("2_camera.txt","r")
   elif var.get() == 3:
      fp=open("3_camera.txt","r")  

   for line in fp:
      text.insert(INSERT,line)
      text.insert(INSERT,'\n')
   text.pack()
   
def screen1():
   clear1()
   if var.get() == 1:
      fp=open("1_screen.txt","r")
   elif var.get() == 2:
      fp=open("2_screen.txt","r")
   elif var.get() == 3:
      fp=open("3_screen.txt","r")  

   for line in fp:
      text.insert(INSERT,line)
      text.insert(INSERT,'\n')
   text.pack()
   
def battery1():
   clear1()
   if var.get() == 1:
      fp=open("1_battery.txt","r")
   elif var.get() == 2:
      fp=open("2_battery.txt","r")
   elif var.get() == 3:
      fp=open("3_battery.txt","r")  

   for line in fp:
      text.insert(INSERT,line)
      text.insert(INSERT,'\n')
   text.pack()
   
def performance1():
   clear1()
   if var.get() == 1:
      fp=open("1_performance.txt","r")
   elif var.get() == 2:
      fp=open("2_performance.txt","r")
   elif var.get() == 3:
      fp=open("3_performance.txt","r")  

   for line in fp:
      text.insert(INSERT,line)
      text.insert(INSERT,'\n')
   text.pack()

def clear1():
     text.delete("1.0",END)
   
def sel1():

   global root2
   root2=Tk()
   tmp()
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)
   
   frame = Frame(root2)
   frame.pack()
   
   camera = Button(frame,width=15,height=3, text = "CAMERA", fg="red", command = camera1)
   camera.pack(side = LEFT)

   screen = Button(frame,width=15,height=3, text = "SCREEN", fg="blue", command = screen1)
   screen.pack(side = LEFT)

   battery = Button(frame,width=15,height=3, text = "BATTERY", fg="orange", command = battery1)
   battery.pack(side = LEFT)

   performance = Button(frame,width=15,height=3, text = "PERFORMANCE", fg="black", command = performance1)
   performance.pack(side = LEFT)

   graph = Button(frame,width=15,height=3, text = "GRAPH", fg="brown",command=open1)
   graph.pack(side = LEFT)

   root2.mainloop()
      
   clear = Button(frame,width=15,height=3, text = "CLEAR", fg="darkgreen",command=clear1)
   clear.pack(side = LEFT)   


def mod4():
   global root2
   root2=Tk()
   tmp()
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)
   
   frame = Frame(root2)
   frame.pack()
   
   camera = Button(frame,width=15,height=3, text = "RECOMMENDER", fg="red", command = recopro)
   camera.pack(side = LEFT)

   screen = Button(frame,width=15,height=3, text = "RESULT_GRAPH", fg="blue", command = fingraph)
   screen.pack(side = LEFT)

   

root = Tk()
var = IntVar()

w = Label(root,width=15,height=2, text="RecoProd", font=("Helvetica", 35))
w.pack()

R1 = Radiobutton(root,width=15,height=2, text="PRODUCT A", variable=var, value=1,command=sel1)
R1.pack( anchor = W )

R2 = Radiobutton(root,width=15,height=2, text="PRODUCT B", variable=var, value=2,command=sel1)
R2.pack( anchor = W )

R3 = Radiobutton(root,width=15,height=2, text="PRODUCT C", variable=var, value=3,command=sel1)
R3.pack( anchor = W)

R3 = Radiobutton(root,width=15,height=2, text="RESULT", variable=var, value=4,command=mod4)
R3.pack( anchor = W)

label = Label(root)
label.pack()
root.mainloop()
