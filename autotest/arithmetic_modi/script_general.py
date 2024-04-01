import os
import glob
import subprocess
import tqdm
command = "iverilog" #please install iverilog
dir_base = "/home/datasets/DAC_openSource/autotest/arithmetic_modi/" #the dir where cases saved
sourcemodel = "" #the model which generate the verilog code

dir_sub = [subd for subd in os.listdir(dir_base) if os.path.isdir(subd) if subd!="multi_booth_"] #the subdir in basedir should be "1.accu"
cmdlist = [] #save the input file of the iverilog command
# for item_sub_dir in dir_sub:
#     if(len(glob.glob(dir_base+item_sub_dir+"/"+sourcemodel+"*.v"))):
#         if(os.path.isfile(dir_base+item_sub_dir+"/testbench.v")):
#             cmdlist.append(glob.glob(dir_base+item_sub_dir+"/"+sourcemodel+"*.v")[0]+" "+dir_base+item_sub_dir+"/testbench.v")
# for item_sub_dir in dir_sub:
#     designfilelist = [designfile for designfile in os.listdir(item_sub_dir) if designfile!="testbench.v"]
#     for item_design in designfilelist:
#         cmdlist.append(dir_base+item_sub_dir+item_design+" "+dir_base+item_sub_dir+"/testbench.v")
#         print(dir_base+item_sub_dir+item_design)

for item_sub_dir in dir_sub:
    # print(item_sub_dir)
    # print(os.listdir(item_sub_dir))
    designfilelist = [designfile for designfile in os.listdir(item_sub_dir) if designfile!="testbench.v"]
    # print(designfilelist)
    for item_design in designfilelist:
        designcode = [item for item in os.listdir(dir_base+item_sub_dir+"/"+item_design) if item!="testbench.v" and item != "a.out"][0]
        cmdlist.append(dir_base+item_sub_dir+"/"+item_design+"/"+designcode+" "+dir_base+item_sub_dir+"/"+item_design+"/"+"testbench.v")

resultlist= [] #save the result

for i in tqdm.tqdm(cmdlist):

    # print(command+" "+i) #print the command
    result = subprocess.run(command+" "+i, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True, cwd = os.path.dirname(i.split(" ")[0])) #run command
    # if subprocess.TimeoutExpired:
    #     resultlist.append("----------------------------\n"+"design: "+i.split(" ")[0].split("/")[-1]+"\nTime out.\n"+"----------------------------\n")
    #     continue
    # try:
    #     result = subprocess.run(command+" "+i, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True, cwd = os.path.dirname(i.split(" ")[0]), timeout=1, check=True) #run command
    #     if(result.returncode==0):
    #     # resultlist.append(i.split(" ")[0]+", "+"syntax correct\n")
    #     # print("vvp"+" "+os.path.dirname(i.split(" ")[0])+"/a.out")
    #         resultfunc = subprocess.run("vvp"+" "+os.path.dirname(i.split(" ")[0])+"/a.out", shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True, cwd = os.path.dirname(i.split(" ")[0]))
    #         resultlist.append("----------------------------\n"+"design: "+i.split(" ")[0].split("/")[-1]+"\nsyntax: "+"syntax correct\n"+"function: "+resultfunc.stdout+"\n"+"----------------------------\n")
    #     else:
    #         resultlist.append("----------------------------\n"+"design: "+i.split(" ")[0].split("/")[-1]+"\nsyntax: "+"syntax error\n"+"detail: "+result.stderr+"\n"+"----------------------------\n")
    # except subprocess.TimeoutExpired:
    #     resultlist.append("----------------------------\n"+"design: "+i.split(" ")[0].split("/")[-1]+"\nTime out.\n"+"----------------------------\n")
    #     continue
    # except subprocess.CalledProcessError:
    #     continue
    if(result.returncode==0):
        
        # resultfunc = subprocess.run("vvp"+" "+os.path.dirname(i.split(" ")[0])+"/a.out", shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True, cwd = os.path.dirname(i.split(" ")[0]))
        # resultlist.append("----------------------------\n"+"design: "+i.split(" ")[0].split("/")[-1]+"\nsyntax: "+"syntax correct\n"+"function: "+resultfunc.stdout+"\n"+"----------------------------\n")
        try:
            resultfunc = subprocess.run("vvp"+" "+os.path.dirname(i.split(" ")[0])+"/a.out", shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True, cwd = os.path.dirname(i.split(" ")[0]),timeout=3,check=True)
            # resultlist.append("----------------------------\n"+"design: "+i.split(" ")[0].split("/")[-1]+"\nsyntax: "+"syntax correct\n"+"function: "+resultfunc.stdout+"\n"+"----------------------------\n")
            resultlist.append("----------------------------\n"+"design: "+i.split(" ")[0]+"\nsyntax: "+"syntax correct\n"+"function: "+resultfunc.stdout+"\n"+"----------------------------\n")
        except subprocess.TimeoutExpired:
            # resultlist.append("----------------------------\n"+"design: "+i.split(" ")[0].split("/")[-1]+"\nsyntax: "+"syntax correct\n"+"function: a.out read error"+resultfunc.stdout+"\n"+"----------------------------\n")
            resultlist.append("----------------------------\n"+"design: "+i.split(" ")[0]+"\nsyntax: "+"syntax correct\n"+"function: a.out read error"+resultfunc.stdout+"\n"+"----------------------------\n")
            continue
        except subprocess.CalledProcessError:
            # resultlist.append("----------------------------\n"+"design: "+i.split(" ")[0].split("/")[-1]+"\nsyntax: "+"syntax correct\n"+"function: a.out read error"+resultfunc.stdout+"\n"+"----------------------------\n")
            resultlist.append("----------------------------\n"+"design: "+i.split(" ")[0]+"\nsyntax: "+"syntax correct\n"+"function: a.out read error"+resultfunc.stdout+"\n"+"----------------------------\n")
            continue
    else:
        # resultlist.append("----------------------------\n"+"design: "+i.split(" ")[0].split("/")[-1]+"\nsyntax: "+"syntax error\n"+"detail: "+result.stderr+"\n"+"----------------------------\n")
        resultlist.append("----------------------------\n"+"design: "+i.split(" ")[0]+"\nsyntax: "+"syntax error\n"+"detail: "+result.stderr+"\n"+"----------------------------\n")
resultfile = "/home/datasets/DAC_openSource/autotest/arithmetic_modi/resulttestzyh.txt" #the output file
with open(resultfile,'w') as f:
    for item in resultlist:
        f.write(item)