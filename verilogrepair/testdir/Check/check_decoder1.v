4. Executing CHECK pass (checking for obvious problems).
Checking module encorder...
Warning: multiple conflicting drivers for encorder.$logic_or$./testdir/Wrong/wrong_decoder1.v:26$4_Y:
    port Y[0] of cell $logic_or$./testdir/Wrong/wrong_decoder1.v:26$4 ($logic_or)
    port Y[0] of cell $or$./testdir/Wrong/wrong_decoder1.v:10$1 ($or)
    module input in1[0]
Warning: found logic loop in module encorder:
    cell $logic_and$./testdir/Wrong/wrong_decoder1.v:25$3 ($logic_and)
    cell $logic_or$./testdir/Wrong/wrong_decoder1.v:26$4 ($logic_or)
    wire $logic_and$./testdir/Wrong/wrong_decoder1.v:25$3_Y
    wire $logic_or$./testdir/Wrong/wrong_decoder1.v:26$4_Y
Found and reported 2 problems.

Warnings: 2 unique messages, 2 total
End of script. Logfile hash: 9cc7727256, CPU: user 0.00s system 0.00s, MEM: 11.77 MB peak
