4. Executing CHECK pass (checking for obvious problems).
Checking module counter...
Warning: multiple conflicting drivers for counter.$or$./testdir/Wrong/wrong_count.v:6$1_Y [0]:
    port Y[0] of cell $or$./testdir/Wrong/wrong_count.v:6$1 ($or)
    module input en[0]
Warning: multiple conflicting drivers for counter.$logic_or$./testdir/Wrong/wrong_count.v:15$5_Y:
    port Y[0] of cell $logic_or$./testdir/Wrong/wrong_count.v:15$5 ($logic_or)
    module input rst[0]
Warning: found logic loop in module counter:
    cell $logic_and$./testdir/Wrong/wrong_count.v:14$4 ($logic_and)
    cell $logic_or$./testdir/Wrong/wrong_count.v:15$5 ($logic_or)
    wire $logic_and$./testdir/Wrong/wrong_count.v:14$4_Y
    wire $logic_or$./testdir/Wrong/wrong_count.v:15$5_Y
Found and reported 3 problems.

Warnings: 3 unique messages, 3 total
End of script. Logfile hash: 56cdbe47d9, CPU: user 0.00s system 0.00s, MEM: 11.55 MB peak
