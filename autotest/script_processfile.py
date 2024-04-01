import glob
import os
import subprocess
basepath = "/home/zyh/Desktop/gpt-4_rebuttal/advanced/"

listfile = [item for item in os.listdir(basepath) if item[-2:]!="py" and os.path.isfile(basepath+item)]
# print(listfile)
for i in listfile:
    commandmkdir = "mkdir -p "+basepath+i[:-3]
    subprocess.run(commandmkdir, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True)
    
    commandmv = "mv "+basepath+i+" "+basepath+i[:-3]
    subprocess.run(commandmv, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True)