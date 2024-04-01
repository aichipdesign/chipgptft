import glob
import os
import subprocess
basepath = "/home/zyh/Desktop/gpt-4_rebuttal/advanced/"
listfold = [item for item in os.listdir(basepath) if os.path.isdir(basepath+item)]
# print(listfold)
for ifold in listfold:
    listfile = [item for item in os.listdir(basepath+ifold) if item != "testbench.v" and os.path.isfile(basepath+ifold+"/"+item)]
    # print(listfile)
    for ifile in listfile:
        commandmkdir = "mkdir -p "+basepath+ifold+"/"+ifile[:-2]
        # print(commandmkdir)
        subprocess.run(commandmkdir, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True)
        commandmv = "mv "+basepath+ifold+"/"+ifile+" "+basepath+ifold+"/"+ifile[:-2]
        subprocess.run(commandmv, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True)
for ifold in listfold:
    listcase = [item for item in os.listdir(basepath+ifold) if os.path.isdir(basepath+ifold+"/"+item)]
    # print(listcase)
    testbenchpath = basepath+ifold+"/"+"testbench.v"
    # print(testbenchpath)
    for itemcase in listcase:
        # if not os.path.exists(basepath+ifold+"/"+itemcase+"/"+"testbench.v"):
        commandcp = "cp "+testbenchpath+" "+basepath+ifold+"/"+itemcase
        subprocess.run(commandcp, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True)

for ifold in listfold:
    listcase = [item for item in os.listdir(basepath+ifold) if os.path.isdir(basepath+ifold+"/"+item)]
    # print(listcase)
    for itemcase in listcase:
        designfile = [item for item in os.listdir(basepath+ifold+"/"+itemcase) if item!="testbench.v"][0]
        # print(designfile)
        pathdesignfile = basepath+ifold+"/"+itemcase+"/"+designfile
        # print(pathdesignfile)
        # print(designfile)
        with open(pathdesignfile,"r") as f:
            i = 0
            while(1):
                content = f.readline()
                i+=1
                if "module" in content:
                    break
                if i==10:
                    break
        if "module" in content:
            newname = content.split("module")[1].split("(")[0].strip()
            # print(os.path.dirname(pathdesignfile))
            commandrn = "mv "+pathdesignfile+" "+os.path.dirname(pathdesignfile)+"/"+newname+".v"
            subprocess.run(commandrn, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True)