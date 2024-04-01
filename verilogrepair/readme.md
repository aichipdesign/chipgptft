testdir是测试样例，testorigin是原始代码的文件夹。
testrelated是运行时中间文件
generate_json 是最终生成json的py程序
verilog-grammars是antlr的相关文件和一些解析verilog的语法文件。
mutate 是故意犯错程序，因为原始verilog代码错误太少，大部分没有错误，所以故意随机添加错误。
server是核心程序。将一个verilog代码预处理，去掉前置文件，然后经过mutate，最后通过yosys进行纠错。

使用方法
首先有代码存在testdir/testorigin
运行 bash server.sh 
testdir文件夹下出现相关文件
运行 python generate_json.py 
形成 eda_feedbak.json


