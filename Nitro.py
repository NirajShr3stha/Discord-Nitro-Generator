from tkinter import *
from subprocess import Popen
from PIL import ImageTk
from PIL import Image
import PIL
import subprocess
import time
import tkinter as Tk


open("src/var", "w")
with open("src/var", "w") as var_clear:
    var_clear.write("0")
    var_clear.close()

process = subprocess.Popen(["python", "src/SMALL.py"])

root = Tk.Tk()
root.iconbitmap("src/ico.ico")
root.title('XDWOLF')
root.geometry('200x60')
root.resizable(width=False, height=False)
root.configure(bg='#303030')




def start_nitro():
    print("start_nitro")
    process = subprocess.Popen(["python", "Nitro#/Nitro#1.py"])
    time.sleep(2)
    process = subprocess.Popen(["python", "Nitro#/Nitro#2.py"])
    time.sleep(2)
    process = subprocess.Popen(["python", "Nitro#/Nitro#3.py"])
    time.sleep(2)
    process = subprocess.Popen(["python", "Nitro#/Nitro#4.py",])
    time.sleep(2)
    process = subprocess.Popen(["python", "Nitro#/Nitro#5.py"])

def stop_nitro():
	print("Stopping Generator!!")
	print ('EXIT')
	with open("src/var", "w") as var:
    		var.write("1")


btn = Tk.Button(root, text = 'Start Gen', command = start_nitro)
btn.pack()
btn = Tk.Button(root, text = 'Stop Gen', command = stop_nitro)
btn.pack()

root.mainloop()
