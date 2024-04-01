
module carry_select_adder_16bit(a, b, cin, sum, cout);
    input [15:0] a, b;
    input cin;
    output [15:0] sum;
    output cout;

    wire [3:0] sum0_low, sum1_low;
    wire [3:0] sum0_high, sum1_high;
    wire carry0_low,carry1_low,carry0_high,carry1_high;
    wire carry_low, carry_high;
    
    // Lower 4-bit ripple-carry adders
    ripple_carry_adder_4bit adder0_low(
        .a(a[3:0]),
        .b(b[3:0]),
        .cin(1'b0),
        .sum(sum0_low),
        .cout(carry0_low)
    );

    ripple_carry_adder_4bit adder1_low(
        .a(a[3:0]),
        .b(b[3:0]),
        .cin(1'b1),
        .sum(sum1_low),
        .cout(carry1_low)
    );

    // Multiplexer for lower 4-bit sum
    assign {carry_low, sum[3:0]} = cin ? {carry1_low, sum1_low} : {carry0_low, sum0_low};

    // Higher 12-bit ripple-carry adders
    genvar i;
    generate
        for(i = 0; i < 3; i = i + 1) begin : gen_block
            ripple_carry_adder_4bit adder0_high(
                .a(a[4*i+7:4*i+4]),
                .b(b[4*i+7:4*i+4]),
                .cin(1'b0),
                .sum(sum0_high),
                .cout(carry0_high)
            );

            ripple_carry_adder_4bit adder1_high(
                .a(a[4*i+7:4*i+4]),
                .b(b[4*i+7:4*i+4]),
                .cin(1'b1),
                .sum(sum1_high),
                .cout(carry1_high)
            );

            // Multiplexer for higher 4-bit sums
            assign {carry_high, sum[4*i+7:4*i+4]} = carry_low ? {carry1_high, sum1_high} : {carry0_high, sum0_high};
            assign carry_low = carry_high;
        end
    endgenerate

    // Final carry output
    assign cout = carry_high;

endmodule

// 4-bit ripple carry adder module
module ripple_carry_adder_4bit(a, b, cin, sum, cout);
    input [3:0] a, b;
    input cin;
    output [3:0] sum;
    output cout;

    wire [2:0] carry;

    full_adder fa0(
        .a(a[0]),
        .b(b[0]),
        .cin(cin),
        .s(sum[0]),
        .cout(carry[0])
    );

    full_adder fa1(
        .a(a[1]),
        .b(b[1]),
        .cin(carry[0]),
        .s(sum[1]),
        .cout(carry[1])
    );

    full_adder fa2(
        .a(a[2]),
        .b(b[2]),
        .cin(carry[1]),
        .s(sum[2]),
        .cout(carry[2])
    );

    full_adder fa3(
        .a(a[3]),
        .b(b[3]),
        .cin(carry[2]),
        .s(sum[3]),
        .cout(cout)
    );
endmodule

// Full adder module
module full_adder(a, b, cin, s, cout);
    input a, b, cin;
    output s, cout;

    assign s = a ^ b ^ cin;
    assign cout = (a & b) | (b & cin) | (a & cin);
endmodule