import json
import subprocess
import os
import random
import time
from generate import AstTraveller

def run_analysis(file_path):
    # analysis_output = subprocess.check_output(["python", "generate.py", file_path], universal_newlines=True)
    traveller = AstTraveller(file_path)
    analysis_output = traveller.travel_ast()
    return analysis_output

def read_source_code(file_path):
    with open(file_path, "r") as source_file:
        source_code = source_file.read()
    return source_code

def polish_instruction():
    instruction_expressions = [
        "Analyze the provided code to extract relevant insights.",
        "Conduct program analysis to uncover valuable information.",
        "Perform an examination of the given code and output insights.",
        "Carry out a program analysis to reveal important details.",
        "Conduct an analysis of the given code to extract insights.",
        "Perform a thorough examination of the provided program and output relevant details.",
        "Explore the provided code and generate useful insights through program analysis.",
        "Carry out code analysis to uncover valuable information.",
        "Examine the program code and provide insightful analysis results.",
        "Analyze the code snippet to produce informative output.",
        "Investigate the provided code and output meaningful analysis results.",
        "Conduct a comprehensive examination of the code and provide analysis insights.",
        "Perform program analysis to extract valuable information from the code.",
        "Explore the provided code snippet and generate informative analysis output.",
        "Analyze the program code to reveal important insights and information.",
        "Examine the code and output insightful analysis results.",
        "Carry out a detailed analysis of the code to uncover relevant information.",
        "Investigate the code snippet and provide comprehensive analysis output."
    ]
    translated_instruction = random.choice(instruction_expressions)
    return translated_instruction

# analysis_folder_path = "../test_cases/"
# source_folder_path = "../test_cases/"
source_folder_path = "../../extracted_files/folder_"
output_folder_path = "../../prompt_files/"

data = []
total_num = 0
num = 0

for i in range(20, 30):
    st = time.time()
    test_case_files = os.listdir(source_folder_path + str(i))
    print(f"[FUNC_ANALYSIS][FOLDER] : processing {source_folder_path + str(i)}")
    for test_case_file in test_case_files:
        # if random.random() < 1:
        analysis_file_path = os.path.join(source_folder_path + str(i), test_case_file)
        source_file_path = os.path.join(source_folder_path + str(i), test_case_file)
        try:
            print(f"[FUNC_ANALYSIS][{i}][FILE] : processing {test_case_file}, have generated {num} prompts.")
            if os.path.getsize(analysis_file_path) <= 5000:
                analysis_info = run_analysis(analysis_file_path)
                source_code = read_source_code(source_file_path)
                # translated_instruction = polish_instruction()
                # analysis_lines = analysis_info.splitlines()
                # for line in analysis_info:
                translated_instruction = "Please generate verilog code according to the following description"
                prompt = {
                    "instruction": translated_instruction,
                    "input": analysis_info,
                    "output": source_code
                }
                data.append(prompt)
                num += 1
        except Exception as e:
            print(f"[ERROR] : when processing file {source_file_path}. An error occurred: {str(e)}")
            continue 

        # if total_num + num >= 30000:
        #     break

            # if (total_num + num) % 20000 == 0:
            #     num += 1
            #     output_file_path = output_folder_path + "func_analysis_folder_1-10_{}.json".format((total_num + num)//20000)
            #     with open(output_file_path, "w") as json_file:
            #         json.dump(data, json_file, indent=4)
            #     data = []
            #     print(f"[FUNC_ANALYSIS][PROMPT] : 20000条大小的Prompts文件生成成功! 保存在：{output_file_path}, 总promp目前{total_num+num-1}条")
        # else:
        #     pass
    


    
    et = time.time()
    elapsed_time = et - st
    print(f"[FUNC_ANALYSIS][FOLDER] : generated {num} prompts from {source_file_path + str(i)}, consuming {elapsed_time} seconds")
    total_num += num
    num = 0


output_file_path = output_folder_path + "nl_generation_20-29.json"
with open(output_file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)
print(f"[FUNC_ANALYSIS][PROMPT] : Prompts文件生成成功! 一共{total_num}条，保存在：{output_file_path}")
