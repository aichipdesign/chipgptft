import json
import subprocess
import os
import random

def run_analysis(file_path):
    analysis_output = subprocess.check_output(["python", "generate.py", file_path], universal_newlines=True)
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

analysis_folder_path = "../test_cases/"
source_folder_path = "../test_cases/"

test_case_files = os.listdir(analysis_folder_path)
data = []
num = 0

for test_case_file in test_case_files:
    analysis_file_path = os.path.join(analysis_folder_path, test_case_file)
    source_file_path = os.path.join(source_folder_path, test_case_file)
    analysis_info = run_analysis(analysis_file_path)
    source_code = read_source_code(source_file_path)
    # translated_instruction = polish_instruction()
    analysis_lines = analysis_info.splitlines()
    for line in analysis_lines:
        translated_instruction = polish_instruction()
        prompt = {
            "instruction": translated_instruction,
            "input": source_code,
            "output": line
        }
        data.append(prompt)
        num += 1

output_file_path = "prompts.json"
with open(output_file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)

print(f"Prompts文件生成成功！一共{num}条，保存在：{output_file_path}")
