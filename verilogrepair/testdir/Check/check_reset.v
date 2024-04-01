4. Executing CHECK pass (checking for obvious problems).
Checking module reset...
Warning: Wire reset.\out_n is used but has no driver.
Warning: Wire reset.\rst_n_out is used but has no driver.
Warning: found logic loop in module reset:
    cell $logic_and$./testdir/Wrong/wrong_reset.v:55$2 ($logic_and)
    cell $logic_or$./testdir/Wrong/wrong_reset.v:56$3 ($logic_or)
    wire $logic_and$./testdir/Wrong/wrong_reset.v:55$2_Y
    wire $logic_or$./testdir/Wrong/wrong_reset.v:56$3_Y
Found and reported 3 problems.

Warnings: 5 unique messages, 5 total
End of script. Logfile hash: 23f79272a1, CPU: user 0.01s system 0.00s, MEM: 11.92 MB peak
