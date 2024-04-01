import json
import subprocess
import os
import re
import time
import random
from mutate import AstTraveller, MaskRules, ModifyRules

def read_source_code(file_path):
    with open(file_path, "r") as source_file:
        source_code = source_file.read()

    module_pattern = r"(?ms)module(.*?)endmodule"
    matches = re.findall(module_pattern, source_code)
    module_content = "\n".join(["module" + match + "endmodule\n" for match in matches])

    return module_content
    # return source_code


source_folder_path = "../../extracted_files/folder_"
output_folder_path = "../../prompt_files/"
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)
data = []
num = 0
total_num = 0
stt = time.time()

for i in range(25, 36):
    st = time.time()
    test_case_files = os.listdir(source_folder_path + str(i))
    print(f"[CODE_MASK][FOLDER] : begin processing {source_folder_path + str(i)}")
    for test_case_file in test_case_files:
        if random.random() < 0.4:
            source_file_path = os.path.join(source_folder_path + str(i), test_case_file)
            try:
                print(f"[CODE_MASK][FILE] : processing {test_case_file}, have generated {num} prompts.")
                source_code = read_source_code(source_file_path)
                traveller = AstTraveller(source_file_path)
                index_info = traveller.travel_ast().index_info
                masked_code = MaskRules(source_file_path, index_info).modify_code()
            
                prompt = {
                            "instruction": "Please replace the mask word/sentence so that the verilog code is correct "
                                    ", you can analyse it step by step",
                            "input": masked_code,
                            "output": source_code
                        }
                data.append(prompt)
                num += 1
            except Exception as e:
                print(f"[ERROR] : when processing file {source_file_path}. An error occurred: {str(e)}")
                continue 

    et = time.time()
    elapsed_time = et - st
    print(f"[CODE_MASK][FOLDER] : generated {num} prompts from {source_file_path + str(i)}, consuming {elapsed_time} seconds")
    total_num += num
    num = 0


output_file_path = output_folder_path + "code_mask_folder_25-35.json"#.format(total_num//20000+1)
with open(output_file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)
ett = time.time()
elapsed_time = ett - stt
print(f"[CODE_MASK][PROMPT] : Prompts文件生成成功! 保存在：{output_file_path}.一共{total_num}条.总时间消耗{elapsed_time}秒")


