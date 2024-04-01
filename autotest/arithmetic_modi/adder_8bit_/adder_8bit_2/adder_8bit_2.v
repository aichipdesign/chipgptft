
// Define a 1-bit full adder module for reuse in 8-bit adder
module full_adder(
    input a,
    input b,
    input cin,
    output sum,
    output cout
);
    // Gate level implementation of a full adder
    wire xor_ab, and_ab, and_cinxor_ab;
    xor(xor_ab, a, b);        // xor gate for a and b
    and(and_ab, a, b);        // and gate for a and b
    xor(sum, xor_ab, cin);    // xor gate for xor_ab and cin
    and(and_cinxor_ab, xor_ab, cin); // and gate for cin and xor_ab
    or(cout, and_ab, and_cinxor_ab); // or gate for and_ab and and_cinxor_ab
endmodule

// Define the 8-bit adder module using 1-bit full adder modules
module adder_8bit(
    input [7:0] a,
    input [7:0] b,
    input cin,
    output [7:0] sum,
    output SUM,
    output cout
);
    // Internal signals to carry out the carry bit from one full adder to the next
    wire [6:0] carry;

    // Instantiate 8 full adder modules
    full_adder fa0(a[0], b[0], cin, sum[0], carry[0]);
    full_adder fa1(a[1], b[1], carry[0], sum[1], carry[1]);
    full_adder fa2(a[2], b[2], carry[1], sum[2], carry[2]);
    full_adder fa3(a[3], b[3], carry[2], sum[3], carry[3]);
    full_adder fa4(a[4], b[4], carry[3], sum[4], carry[4]);
    full_adder fa5(a[5], b[5], carry[4], sum[5], carry[5]);
    full_adder fa6(a[6], b[6], carry[5], sum[6], carry[6]);
    full_adder fa7(a[7], b[7], carry[6], sum[7], cout);

    // Set SUM to the XOR of all bits in the sum to represent an even parity bit
    assign SUM = ^(sum);
endmodule