import tkinter, tkinter.filedialog
import os
root = tkinter.Tk()
dirname = tkinter.filedialog.askdirectory(parent=root,initialdir="/home",title='Please select a directory')
if len(dirname ) > 0:
    print(dirname)
os.system('python3 maincheck.py')
root.mainloop()
