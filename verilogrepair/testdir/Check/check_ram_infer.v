4. Executing CHECK pass (checking for obvious problems).
Checking module ram_infer...
Warning: multiple conflicting drivers for ram_infer.$or$./testdir/Wrong/wrong_ram_infer.v:58$78_Y [7]:
    port Y[7] of cell $or$./testdir/Wrong/wrong_ram_infer.v:58$78 ($or)
    module input dina[7]
Warning: multiple conflicting drivers for ram_infer.$or$./testdir/Wrong/wrong_ram_infer.v:58$78_Y [6]:
    port Y[6] of cell $or$./testdir/Wrong/wrong_ram_infer.v:58$78 ($or)
    module input dina[6]
Warning: multiple conflicting drivers for ram_infer.$or$./testdir/Wrong/wrong_ram_infer.v:58$78_Y [5]:
    port Y[5] of cell $or$./testdir/Wrong/wrong_ram_infer.v:58$78 ($or)
    module input dina[5]
Warning: multiple conflicting drivers for ram_infer.$or$./testdir/Wrong/wrong_ram_infer.v:58$78_Y [4]:
    port Y[4] of cell $or$./testdir/Wrong/wrong_ram_infer.v:58$78 ($or)
    module input dina[4]
Warning: multiple conflicting drivers for ram_infer.$or$./testdir/Wrong/wrong_ram_infer.v:58$78_Y [3]:
    port Y[3] of cell $or$./testdir/Wrong/wrong_ram_infer.v:58$78 ($or)
    module input dina[3]
Warning: multiple conflicting drivers for ram_infer.$or$./testdir/Wrong/wrong_ram_infer.v:58$78_Y [2]:
    port Y[2] of cell $or$./testdir/Wrong/wrong_ram_infer.v:58$78 ($or)
    module input dina[2]
Warning: multiple conflicting drivers for ram_infer.$or$./testdir/Wrong/wrong_ram_infer.v:58$78_Y [1]:
    port Y[1] of cell $or$./testdir/Wrong/wrong_ram_infer.v:58$78 ($or)
    module input dina[1]
Warning: multiple conflicting drivers for ram_infer.$or$./testdir/Wrong/wrong_ram_infer.v:58$78_Y [0]:
    port Y[0] of cell $or$./testdir/Wrong/wrong_ram_infer.v:58$78 ($or)
    module input dina[0]
Warning: multiple conflicting drivers for ram_infer.$logic_or$./testdir/Wrong/wrong_ram_infer.v:69$91_Y:
    port Y[0] of cell $logic_or$./testdir/Wrong/wrong_ram_infer.v:69$91 ($logic_or)
    module input ena[0]
Warning: found logic loop in module ram_infer:
    cell $logic_and$./testdir/Wrong/wrong_ram_infer.v:68$90 ($logic_and)
    cell $logic_or$./testdir/Wrong/wrong_ram_infer.v:69$91 ($logic_or)
    wire $logic_and$./testdir/Wrong/wrong_ram_infer.v:68$90_Y
    wire $logic_or$./testdir/Wrong/wrong_ram_infer.v:69$91_Y
Found and reported 10 problems.

Warnings: 10 unique messages, 10 total
End of script. Logfile hash: 4a8eac10a5, CPU: user 0.02s system 0.00s, MEM: 13.55 MB peak
