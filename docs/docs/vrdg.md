# Verilog Repair data generating

author：Wenlong Zhu

There are multiple files in this folder(verilogrepair), among which verilog-grammars is the relevant dependency package, server.sh is the main script for data generation, generate_json is the json generation program, testdir is the sample folder, and testrelated is the auxiliary file when the sample is run. 
The specific usage is as follows:
1. Get the initial code
Add the code that requires data enhancement to the testdir/testorigin folder (this folder already has sample code).
2. Data enhancement
Run the command bash server.sh from the command line
3. Data augmentation results
After successful operation, the testdir/Check, testdir/Right, and testdir/Wrong folders will appear under the testdir folder. Check is the error message synthesized by yosys, Right is the processed original code, and Wrong is the error-processed code.
4. Generate json
Run python generate_json.py from the command line
5. json result
After the operation is successful, the eda_feedback.json file appears, and this file is the final result.
6. mutate suggestion
If you need to modify the related error adding program, modify the verilog-grammars/mutate.py folder.
7. yosys command suggestions
If you need to use the relevant optimization commands of yosys to regenerate the verilog code, please modify the yosys script at line 59 of server.sh, add relevant statements such as 'write_verilog' and perform relevant output. This optimization is better, but after yosys rewrite Code readability is extremely low.