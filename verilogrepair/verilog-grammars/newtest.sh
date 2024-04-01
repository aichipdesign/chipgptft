#!/bin/bash
Right_code_dir="/mnt/d/Right"
Wrong_code_dir="/mnt/d/Wrongt"

Right_codes_=$(ls "$Right_code_dir")

for Right_code in $Right_codes_; do
  #echo $Right_code
  #echo $tempname
  Wrong_code="Wrongcode_${Right_code:10}"
  echo $Wrong_code
  #echo  python3 mutate.py $Right_code_dir/$Right_code
  `echo  python3 mutate.py $Right_code_dir/$Right_code` > "$Wrong_code_dir/$Wrong_code"
  
  echo "==================================="
done
