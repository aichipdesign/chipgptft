
module adder_8bit(
    input [7:0] a,
    input [7:0] b,
    input cin,
    output [7:0] sum,
    output cout
);
    wire [6:0] c; // Internal carry wires
    
    // Instantiate 8 1-bit full adders connecting carry out to carry in of the next.
    full_adder U0 (a[0], b[0], cin, sum[0], c[0]);
    full_adder U1 (a[1], b[1], c[0], sum[1], c[1]);
    full_adder U2 (a[2], b[2], c[1], sum[2], c[2]);
    full_adder U3 (a[3], b[3], c[2], sum[3], c[3]);
    full_adder U4 (a[4], b[4], c[3], sum[4], c[4]);
    full_adder U5 (a[5], b[5], c[4], sum[5], c[5]);
    full_adder U6 (a[6], b[6], c[5], sum[6], c[6]);
    full_adder U7 (a[7], b[7], c[6], sum[7], cout);
    
endmodule

module full_adder(
    input a,
    input b,
    input cin,
    output sum,
    output cout
);
    // XOR gates for sum
    xor (sum, a, b, cin);
    
    // AND/OR gates for carry-out
    wire ab, bc, ca;
    and (ab, a, b);
    and (bc, b, cin);
    and (ca, cin, a);
    or (cout, ab, bc, ca);
    
endmodule