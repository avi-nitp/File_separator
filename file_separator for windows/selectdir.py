import tkinter, tkinter.filedialog
import os
import tkinter.messagebox
import shutil
def dire():
    dirname =tkinter.filedialog.askdirectory(parent=root,initialdir="/home",title='Please select a directory')
    if len(dirname)>0:
        print(dirname)
    return dirname
def sel():
   source =dire()
   with open(source+"/sourcecode.py","a") as f1:
      cw=os.path.dirname(os.path.abspath(__file__))
      shutil.copy2( cw+'/second.py',source+'/sourcecode.py')
      os.chdir(source)
      os.system('py sourcecode.py')
   os.remove("sourcecode.py")
   tkinter.messagebox.showinfo("File separator", "files sorted successfully")
   exit()
def ex():
  exit()
root = tkinter.Tk()
root.title("Avi-Proj-File separator")
root.configure(background="black")

width = 500 # width for the Tk root
height = 350 # height for the Tk root

# get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))

#root.minsize(500,300)
b1=tkinter.Button(root,text="Select directory whose files need to be sorted",command=sel)
b2=tkinter.Button(root,text="Exit",command=ex)
b1.pack(pady=30)
b2.pack()
root.mainloop()
