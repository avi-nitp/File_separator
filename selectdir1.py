import tkinter, tkinter.filedialog
import os
import shutil
def dire():
	dirname =tkinter.filedialog.askdirectory(parent=root,initialdir="/home",title='Please select a directory')
	if len(dirname)>0:
			print(dirname)
	return dirname
def sel():
	source =dire()
	f1=open(source+"/sourcecode.py","a")
	cw=os.path.dirname(os.path.abspath(__file__))
	shutil.copy2( cw+'/second.py',source+'/sourcecode.py')
	os.chdir(source)
	os.system('python3 sourcecode.py')
	os.remove("sourcecode.py")
def ex():
	exit()
root = tkinter.Tk()
root.title("Avi-Proj")
root.configure(background="black")
root.minsize(300,100)
b1=tkinter.Button(root,text="Begin Wizard",command=sel)
b2=tkinter.Button(root,text="Exit",command=ex)
b1.pack()
b2.pack()
root.mainloop()
