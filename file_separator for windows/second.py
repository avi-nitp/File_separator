#Avinash kumar singh project work
#Nit Patna,CSE
#save the two files in some folder somewhere,else may show missing file.
#important:-run (selectdir.py) file first using python IDLE or download python IDE for windows(if u don't have) to run it.

import shutil
import os

#from maincheck import source
source =os.path.dirname(os.path.abspath(__file__))

#appending of path
dest4 = source+'/Documents'

dest2 = source+'/cpp'

dest3=source+'/c'

dest1=source+'/python'

dest5=source+'/java'

dest6=source+'/Audio'

dest7=source+'/Video'

dest8=source+'/Images'

dest9=source+'/PDF'

dest10=source+'/ExE'

dest11=source+'/Shell'

dest12=source+'/SQL'

dest13=source+'/Others'

#if not os.path.exists(dest1):
 #   os.makedirs(dest1)



files = os.listdir(source)

for f in files:
    if (f.endswith((".py",".py3",".pyc",".pyo",".pyw",".pyx",".pyd",".pxd",".pxi",".pyi",".pyz",".pywz")) and not (f=="sourcecode.py")):
        if not os.path.exists(dest1):
           os.makedirs(dest1)
        shutil.move(f, dest1)
    elif (f.endswith((".cpp",".hpp",".cxx",".cc"))):
         if not os.path.exists(dest2):
            os.makedirs(dest2)
         shutil.move(f, dest2)
    elif (f.endswith(".c")):
         if not os.path.exists(dest3):
            os.makedirs(dest3)
         shutil.move(f, dest3)
    elif (f.endswith((".txt",".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt","pptx"))):
         if not os.path.exists(dest4):
            os.makedirs(dest4)
         shutil.move(f, dest4)
    elif (f.endswith((".java",".class"))):
         if not os.path.exists(dest5):
            os.makedirs(dest5)
         shutil.move(f, dest5)
    elif (f.endswith((".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"))):
         if not os.path.exists(dest6):
            os.makedirs(dest6)
         shutil.move(f, dest6)
    elif (f.endswith((".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"))):
         if not os.path.exists(dest7):
            os.makedirs(dest7)
         shutil.move(f, dest7)
    elif (f.endswith((".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"))):
         if not os.path.exists(dest8):
            os.makedirs(dest8)
         shutil.move(f, dest8)
    elif (f.endswith((".pdf"))):
         if not os.path.exists(dest9):
            os.makedirs(dest9)
         shutil.move(f, dest9)
    elif (f.endswith((".exe"))):
         if not os.path.exists(dest10):
            os.makedirs(dest10)
         shutil.move(f, dest10)
    elif (f.endswith((".sh"))):
         if not os.path.exists(dest11):
            os.makedirs(dest11)
         shutil.move(f, dest11)
    elif (f.endswith((".sql"))):
         if not os.path.exists(dest12):
            os.makedirs(dest12)
         shutil.move(f, dest12)
    else :
         if not os.path.isdir(f):
            if not f=="sourcecode.py":
               if not os.path.exists(dest13):
                  os.makedirs(dest13)
               shutil.move(f, dest13)
#print("executed")
