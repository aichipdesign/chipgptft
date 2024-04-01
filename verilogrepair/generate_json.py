import json
import os



check_load = f"./testdir/Check"
right_load = f"./testdir/Right"
wrong_load = f"./testdir/Wrong"
###
## Checkload is the path of an original file, 
## used to check whether it contains an `include statement,
## code that cannot be synthesized by yosys.
## rightload is a path to remove `include. 
## This path serves as unprocessed source correct code.
## wrongload is the code after adding error processing to the rightload code.
###
json_data = []

with open(f'./testdir/eda_feedbak.json', 'w') as json_file:
    json_file.write("[\n")

    for index, file in enumerate(os.listdir(check_load)):
        number = file[6:].split(".")[0]
        print( number)
        right_name = f"right_{number}.v"
        wrong_name = f"wrong_{number}.v"
        print(right_name)

        with open(f"{wrong_load}/{wrong_name}", 'r') as wrong_file:
            input1 = wrong_file.read()

        with open(f"{check_load}/{file}", 'r') as input_file:
            input2 = input_file.read()

        with open(f"{right_load}/{right_name}", 'r') as right_file:
            output = right_file.read()

        if input1 and input2 and output:
            json_obj = {
                "instruction": "Correct the Verilog code in the input based on EDA tool feedback in the input",
                "input": f"code: {input1}, feedback: {input2}",
                "output": output
            }
            json_data.append(json_obj)
            json_file.write(json.dumps(json_obj))
            
            if index != len(os.listdir(check_load)) - 1:
                json_file.write(",\n")

    json_file.write("\n]\n")

print(f"Converted {len(json_data)} records to JSON.")