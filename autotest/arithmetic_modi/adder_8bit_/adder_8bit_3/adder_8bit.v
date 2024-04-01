
module adder_8bit(
    input [7:0] a,
    input [7:0] b,
    input cin,
    output [7:0] sum,
    output SUM,
    output cout
);
    wire [6:0] c; // Intermediate carry outputs

    // Instantiate the chain of 1-bit full adders
    full_adder fa0 (.a(a[0]), .b(b[0]), .cin(cin),   .sum(sum[0]), .cout(c[0]));
    full_adder fa1 (.a(a[1]), .b(b[1]), .cin(c[0]),  .sum(sum[1]), .cout(c[1]));
    full_adder fa2 (.a(a[2]), .b(b[2]), .cin(c[1]),  .sum(sum[2]), .cout(c[2]));
    full_adder fa3 (.a(a[3]), .b(b[3]), .cin(c[2]),  .sum(sum[3]), .cout(c[3]));
    full_adder fa4 (.a(a[4]), .b(b[4]), .cin(c[3]),  .sum(sum[4]), .cout(c[4]));
    full_adder fa5 (.a(a[5]), .b(b[5]), .cin(c[4]),  .sum(sum[5]), .cout(c[5]));
    full_adder fa6 (.a(a[6]), .b(b[6]), .cin(c[5]),  .sum(sum[6]), .cout(c[6]));
    full_adder fa7 (.a(a[7]), .b(b[7]), .cin(c[6]),  .sum(sum[7]), .cout(cout));

    assign SUM = sum[7]; // Normally, this is done to verify the MSB of the sum

endmodule

// The 1-bit full adder
module full_adder(
    input a,
    input b,
    input cin,
    output sum,
    output cout
);
    // Intermediate signals for gate-level connections
    wire xor_ab, and_ab, and_cin_xor;

    // Implementing the full adder logic
    xor (xor_ab, a, b);      // xor gate for a and b
    xor (sum, xor_ab, cin);  // xor gate for (a xor b) and cin
    
    and (and_ab, a, b);             // and gate for a and b
    and (and_cin_xor, cin, xor_ab); // and gate for cin and (a xor b)
    or  (cout, and_ab, and_cin_xor);// or gate for the two and gates

endmodule