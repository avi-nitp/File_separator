import shutil
import os

#we tried to make this file executable by adding the first line and then changing the mode to executable 
source = '/home/avi/Documents'

#appending of path
dest1 = source+'/textnewfold'

dest2 = '/home/avi/cpp'

#creating of file in different modes
#fl=open(source+"/psource.py","a")

f1=open(source+"/sourcecode.py","a")

#to get current working directory
cw=os.path.dirname(os.path.abspath(__file__))

#copying of file
shutil.copy2(cw+'/second.py',source+'/sourcecode.py')

os.chdir(source)
os.system('python sourcecode.py')

os.remove("sourcecode.py")
