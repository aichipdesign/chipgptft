4. Executing CHECK pass (checking for obvious problems).
Checking module Decoder...
Warning: multiple conflicting drivers for Decoder.$logic_or$./testdir/Wrong/wrong_gate.v:22$18_Y:
    port Y[0] of cell $logic_or$./testdir/Wrong/wrong_gate.v:22$18 ($logic_or)
    port Y[0] of cell $and$./testdir/Wrong/wrong_gate.v:12$4 ($and)
Warning: found logic loop in module Decoder:
    cell $logic_and$./testdir/Wrong/wrong_gate.v:21$17 ($logic_and)
    cell $logic_or$./testdir/Wrong/wrong_gate.v:22$18 ($logic_or)
    wire $logic_and$./testdir/Wrong/wrong_gate.v:21$17_Y
    wire $logic_or$./testdir/Wrong/wrong_gate.v:22$18_Y
Found and reported 2 problems.

Warnings: 2 unique messages, 2 total
End of script. Logfile hash: 85f6811747, CPU: user 0.00s system 0.01s, MEM: 12.50 MB peak
