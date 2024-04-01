4. Executing CHECK pass (checking for obvious problems).
Checking module decoder_using_assign...
Warning: multiple conflicting drivers for decoder_using_assign.$logic_or$./testdir/Wrong/wrong_3-8decoder.v:23$6_Y:
    port Y[0] of cell $logic_or$./testdir/Wrong/wrong_3-8decoder.v:23$6 ($logic_or)
    port Y[0] of cell $or$./testdir/Wrong/wrong_3-8decoder.v:18$1 ($or)
    module input enable[0]
Warning: found logic loop in module decoder_using_assign:
    cell $logic_and$./testdir/Wrong/wrong_3-8decoder.v:22$5 ($logic_and)
    cell $logic_or$./testdir/Wrong/wrong_3-8decoder.v:23$6 ($logic_or)
    wire $logic_and$./testdir/Wrong/wrong_3-8decoder.v:22$5_Y
    wire $logic_or$./testdir/Wrong/wrong_3-8decoder.v:23$6_Y
Found and reported 2 problems.

Warnings: 2 unique messages, 2 total
End of script. Logfile hash: 185ea59bff, CPU: user 0.00s system 0.01s, MEM: 11.99 MB peak
