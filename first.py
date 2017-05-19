import shutil
import os
import tkinter, tkinter.filedialog

import openfile as kk 
source =kk.dirname

#creating of file in different modes
#fl=open(source+"/psource.py","a")

f1=open(source+"/sourcecode.py","a")

#to get current working directory
cw=os.path.dirname(os.path.abspath(__file__))

#copying of file
shutil.copy2(cw+'/second.py',source+'/sourcecode.py')


#runs the new file from this file
os.chdir(source)
os.system('python3 sourcecode.py')

os.remove("sourcecode.py")
