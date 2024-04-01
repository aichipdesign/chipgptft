
module adder_8bit (
    input [7:0] a, b,
    input cin,
    output [7:0] sum,
    output cout
);

wire c1, c2, c3, c4, c5, c6, c7;

// Instantiate 1-bit full adders
full_adder FA0 (.a(a[0]), .b(b[0]), .cin(cin), .sum(sum[0]), .cout(c1));
full_adder FA1 (.a(a[1]), .b(b[1]), .cin(c1), .sum(sum[1]), .cout(c2));
full_adder FA2 (.a(a[2]), .b(b[2]), .cin(c2), .sum(sum[2]), .cout(c3));
full_adder FA3 (.a(a[3]), .b(b[3]), .cin(c3), .sum(sum[3]), .cout(c4));
full_adder FA4 (.a(a[4]), .b(b[4]), .cin(c4), .sum(sum[4]), .cout(c5));
full_adder FA5 (.a(a[5]), .b(b[5]), .cin(c5), .sum(sum[5]), .cout(c6));
full_adder FA6 (.a(a[6]), .b(b[6]), .cin(c6), .sum(sum[6]), .cout(c7));
full_adder FA7 (.a(a[7]), .b(b[7]), .cin(c7), .sum(sum[7]), .cout(cout));

endmodule

// Definition of a 1-bit full adder
module full_adder(
    input a, b, cin,
    output sum, cout
);
    wire s1, c1, c2;

    // Using basic gates for the full adder logic
    xor(s1, a, b);
    xor(sum, s1, cin);
    
    and(c1, a, b);
    and(c2, s1, cin);
    
    or(cout, c1, c2);

endmodule