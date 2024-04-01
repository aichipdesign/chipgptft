
module full_adder(
    input a,
    input b,
    input cin,
    output sum,
    output cout
);
    assign {cout, sum} = a + b + cin;
endmodule

module four_bit_adder_block(
    input [3:0] a,
    input [3:0] b,
    input cin,
    output [3:0] sum,
    output cout
);
    wire [3:1] carry;

    full_adder fa0(a[0], b[0], cin, sum[0], carry[1]);
    full_adder fa1(a[1], b[1], carry[1], sum[1], carry[2]);
    full_adder fa2(a[2], b[2], carry[2], sum[2], carry[3]);
    full_adder fa3(a[3], b[3], carry[3], sum[3], cout);
endmodule

module mux2to1(
    input sel,
    input in0,
    input in1,
    output out
);
    assign out = sel ? in1 : in0;
endmodule

module carry_select_adder_16bit(
    input [15:0] a,
    input [15:0] b,
    input cin,
    output [15:0] sum,
    output cout
);
    wire [3:0] carry; // Intermediate carries
    wire [15:0] sum0, sum1;
    wire [3:0] cout0, cout1;

    // Instantiate the four-bit adder blocks twice for each 4-bit partition
    // First instance assumes carry-in is 0, second assumes carry-in is 1
    genvar i;
    generate
        for (i=0; i < 4; i=i+1) begin : blk
            four_bit_adder_block adder0(
                .a(a[i*4 +: 4]),
                .b(b[i*4 +: 4]),
                .cin(i == 0 ? cin : carry[i-1]),
                .sum(sum0[i*4 +: 4]),
                .cout(cout0[i])
            );

            four_bit_adder_block adder1(
                .a(a[i*4 +: 4]),
                .b(b[i*4 +: 4]),
                .cin(1'b1),
                .sum(sum1[i*4 +: 4]),
                .cout(cout1[i])
            );

            // Select the correct sum and carry based on previous carry
            mux2to1 mux_sum(
                .sel(i == 0 ? cin : carry[i-1]),
                .in0(sum0[i*4 +: 4]),
                .in1(sum1[i*4 +: 4]),
                .out(sum[i*4 +: 4])
            );

            if (i < 3) begin
                mux2to1 mux_carry(
                    .sel(i == 0 ? cin : carry[i-1]),
                    .in0(cout0[i]),
                    .in1(cout1[i]),
                    .out(carry[i])
                );
            end
        end
    endgenerate

    assign cout = carry[3] ? cout1[3] : cout0[3]; // Final carry-out
endmodule