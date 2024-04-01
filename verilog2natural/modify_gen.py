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

    # module_pattern = r"(?ms)module(.*?)endmodule"
    # matches = re.findall(module_pattern, source_code)
    # module_content = "\n".join(["module" + match + "endmodule\n" for match in matches])

    # return module_content
    return source_code


# source_folder_path = "../test_cases/"
source_folder_path = "../../verilog_dataset/extracted_files/folder_"
output_folder_path = "../../data_231114/"
# source_folder_path = "../../shailja/verilog_file"
# output_folder_path = "../../shailja/prompt_file/"
# source_folder_path = "../../mini_data/"
# output_folder_path = "../../mini_data_prompt/"
# output_folder_path = 're_test.json'
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)
data = []
num = 0
total_num = 0
stt = time.time()

for i in range(30, 36):
    st = time.time()
    test_case_files = os.listdir(source_folder_path+str(i))
    print(f"[CODE_MODIFY][FOLDER] : begin processing {source_folder_path+str(i)}")
    # print(f"[CODE_MASK][FOLDER] : begin processing {source_folder_path+str(i)}")
    for test_case_file in test_case_files:
        # if random.random() < 0.4:
        source_file_path = os.path.join(source_folder_path+str(i), test_case_file)
        try:
            # print(f"[CODE_MASK][FILE] : processing {test_case_file}, have generated {num} prompts.")
            print(f"[CODE_MODIFY][FILE] : processing {test_case_file}, have generated {num} prompts.")
            # source_code = read_source_code(source_file_path)
            if os.path.getsize(source_file_path) <= 5000:
                traveller = AstTraveller(source_file_path)
                index_info = traveller.travel_ast().index_info
                # masked_code, source_code, dsc = MaskRules(source_file_path, index_info).modify_code()
                modified_code, _, dsc = ModifyRules(source_file_path, index_info).modify_code()
                output = '\n'.join(dsc)
                
                if dsc != [] :#and len(masked_code)+len(output) < 1500:
                    prompt = {
                                "instruction": "Please replace the mask word/sentence so that the verilog code is correct "\
                                        ", you can analyse it step by step",
                                # "input": masked_code,
                                "input": modified_code,
                                # "output": output
                                "output": output
                            }
                    data.append(prompt)
                    num += 1
                else:
                    pass
        except Exception as e:
            print(f"[ERROR] : when processing file {source_file_path}. An error occurred: {str(e)}")
            continue 

    et = time.time()
    elapsed_time = et - st
    # print(f"[CODE_MASK][FOLDER] : generated {num} prompts from {source_file_path}, consuming {elapsed_time} seconds")
    print(f"[CODE_MODIFY][FOLDER] : generated {num} prompts from {source_file_path}, consuming {elapsed_time} seconds")
    total_num += num
    num = 0


output_file_path = output_folder_path + "modify_30-35.json"#.format(total_num//20000+1)
with open(output_file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)
ett = time.time()
elapsed_time = ett - stt
# print(f"[CODE_MASK][PROMPT] : Prompts文件生成成功! 保存在：{output_file_path}.一共{total_num}条.总时间消耗{elapsed_time}秒")
print(f"[CODE_MODIFY][PROMPT] : Prompts文件生成成功! 保存在：{output_file_path}.一共{total_num}条.总时间消耗{elapsed_time}秒")


