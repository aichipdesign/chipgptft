import csv
import time
import re
import json
import random
import sys


def moduleLevelSplit(verilog_code, matchHeader, out_code):

    ## module_header is the interface of the module
    ## module_body is the body of the module
    module_header = matchHeader.group(0).strip()  
    ## to get the Annotation information before module 
    module_header = verilog_code.split(module_header)[0] + module_header
    module_body = verilog_code.replace(module_header, "").strip()
    
    outcell = {"instruct": "auto complete the module of the give verilog interface.","input":None,"output":None}
    outcell["input"] = module_header
    outcell["output"] = module_body
    out_code.append(outcell)

    return module_header, module_body, out_code
    

def sentenceSplit(module_header, module_body):
    lines = module_body.splitlines()

    lineOfAnnotation = []
    #lineOfHalfAnnotation = []
    CodeList = []
    
    LineOfCode = 0
    for line_number, line in enumerate(lines, start=1):
        LineOfCode = LineOfCode + 1
        # Determine whether it is a Annotation
        if line.lstrip().startswith("//") or line.lstrip().startswith("/*") or line.lstrip().startswith("*/") or line.lstrip().startswith("\""):
            lineOfAnnotation.append(LineOfCode)
        if not line.strip():  
            lineOfAnnotation.append(LineOfCode) 
    
        CodeList.append(line) 
    module_body_code_list = list(range(1, LineOfCode + 1)) 
    
    # result_list records the code （except annotation）
    result_list = [item for item in module_body_code_list if item not in lineOfAnnotation] 
    result_list = [x - 1 for x in result_list]
    # select a sentence randomly
    random_element = random.choice(result_list)
    ## sentence_part1 is input 
    ## sentence_part2 is output
    sentence_part1 = module_header  +  '\n'.join(CodeList[0 : random_element - 1])
    sentence_part2 = CodeList[random_element]

    return sentence_part1, sentence_part2


def sentenceLevelSplit(module_header, module_body, out_code):

    sentence_part1, sentence_part2 = sentenceSplit(module_header, module_body)
    outcell = {"instruct": "auto complete the next sentence of the partial verilog code.","input":None,"output":None}
    outcell["input"] = sentence_part1
    outcell["output"] = sentence_part2
    out_code.append(outcell)

    return out_code

def wordLevelSplit(module_header, module_body, out_code):

    sentence_part1, sentence_part2 = sentenceSplit(module_header, module_body)
    sentence_part2 = re.sub(r'//.*', '', sentence_part2)
    word_list = [item for item in sentence_part2.strip().split(' ') if item != ""]
    if len(word_list) > 1:
        random_word_number = random.randint(0, len(word_list) - 2)
        temp = " ".join(word_list[:random_word_number + 1])
        word_part1 = sentence_part1 + "\n" + "  " + temp
        word_part2 = word_list[random_word_number + 1]
        outcell = {"instruct": "auto complete the next word of the partial verilog code","input":None,"output":None}
        outcell["input"] = word_part1
        outcell["output"] = word_part2
        out_code.append(outcell)

    return  out_code




def main():

    csv.field_size_limit(500 * 1024 * 1024)
    
    csv_file_path = "Verilog_bigquery_GitHub.csv"
    output_file = "result.json"
    
    ##out_code is troublesome
    out_code = []

    with open(csv_file_path, newline='', errors='ignore') as csvfile:
        count = 0
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            # to recive verilog code in csv
            verilog_code = ''
            count = count + 1
            # the 26808th data is wrong
            if count == 26808:
                continue

            # if count == 10:
            #     break
            print(count)
    
            for col in row:
                verilog_code += col

            matchHeader = re.search(r'module\s+[^;]+;', verilog_code, re.DOTALL)
            if matchHeader:
                module_header, module_body, out_code = moduleLevelSplit(verilog_code, matchHeader, out_code)

                lines = module_body.splitlines()
    
                if  10 < len(lines) and  len(lines) < 100:
                    frequency = 4
                elif 100 < len(lines):
                    frequency = 6
                else:
                    frequency = 2  
                
                for i in range(frequency + 1):
                    out_code = sentenceLevelSplit(module_header, module_body, out_code)
                    out_code = wordLevelSplit(module_header, module_body, out_code)
            else:
                print("Module not found in the Verilog code.")

            

            
    with open(output_file,'w') as out_f:
      
        out=json.dumps(out_code)
        out_f.write(out)




if __name__ == "__main__":
    main()