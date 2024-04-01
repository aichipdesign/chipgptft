#!/bin/bash


input_dir="./testdir/testorigin"
Right_dir="./testdir/Right"
python_script="./verilog-grammars/mutate.py"
Wrong_dir="./testdir/Wrong"
Check_dir="./testdir/Check"
ys_script="./testrelated/ysscript.ys"
check_out="./testrelated/check.txt"
################
### input_dir is the relevant code input path
### right_dir is preprocessed code, 
### and the lines containing `include are deleted to facilitate synthesis.
### wrong_dir is the code after adding error processing 
### to the rightload code.
### check_dir is the yosys comprehensive information of the code
###
###########
# 清理输出文件夹
mkdir -p "$Right_dir"
rm -rf "$Right_dir/*"

mkdir -p "$Wrong_dir"
rm -rf "$Wrong_dir/*"

mkdir -p "$Check_dir"
rm -rf "$Check_dir/*"

#i=0

# 遍历文件夹中的文件和子文件夹
for file in "$input_dir"/*; do
    

    if [[ -f "$file" ]]; then
       filename=$(basename "$file")
       right_file="right_$filename"
       wrong_file="wrong_$filename"
       check_file="check_$filename"

      # 去除以"`include"开头的行
      if ! timeout 60s awk '!/^`include/' "$file" > "$Right_dir/$right_file"; then
        echo "Timeout for file $file at awk step."
        continue
      fi
      
      # 执行Python脚本，增加错误
      if ! timeout 60s python3 "$python_script" "$Right_dir/$right_file" > "$Wrong_dir/$wrong_file"; then
        echo "Timeout for file $file at python script step."
        continue
      fi
  
      # 判断输出文件是否为空
      if [[ $(stat -c %s "$Wrong_dir/$wrong_file")  -gt 2 ]]; then
        str="read_verilog -sv $Wrong_dir/$wrong_file"
        
        #yosys脚本获取check信息
        echo -e "$str \nhierarchy \nproc;\ncheck" > "$ys_script"
        if ! timeout 60s yosys $ys_script > "$check_out"; then
          echo "Timeout for file $file at yosys step."
          continue
        fi
        #提取check信息
        output=$(awk '/Executing CHECK pass/,/End of script/' "$check_out")
     
        if [[ "$output" != "" ]]; then
          echo "$output" > "$Check_dir/$check_file"
          echo "$filename have finished."
        fi
      fi
    fi
done

echo "处理完成"