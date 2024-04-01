
module carry_select_adder_16bit(a, b, cin, sum, cout);
  input [15:0] a, b;
  input cin;
  output [15:0] sum;
  output cout;

  wire [3:0] sum0[3:0], sum1[3:0]; // 4-bit sums for cin=0 and cin=1
  wire carry0[3:0], carry1[3:0];    // Carry-outs for cin=0 and cin=1
  wire [2:0] carry_select;           // Carry-select signals for the MUXes

  // Instantiate 4-bit adders
  genvar i;
  generate
    for (i=0; i<4; i=i+1) begin: adder_block
      simple_adder_4bit adder0(a[4*i+3:4*i], b[4*i+3:4*i], 1'b0, sum0[i], carry0[i]);
      simple_adder_4bit adder1(a[4*i+3:4*i], b[4*i+3:4*i], 1'b1, sum1[i], carry1[i]);
    end
  endgenerate

  // Instantiate MUXes
  assign sum[3:0] = sum0[0]; // First 4 bits don't require a MUX
  mux2to1 mux1(sum0[1], sum1[1], carry0[0], sum[4:7]);
  mux2to1 mux2(sum0[2], sum1[2], carry0[1], sum[8:11]);
  mux2to1 mux3(sum0[3], sum1[3], carry0[2], sum[12:15]);

  // Assign carry-out
  mux2to1 mux_carry(carry0[3], carry1[3], carry0[2], cout);

  // Assign carry-select signals
  assign carry_select[0] = cin;
  assign carry_select[1] = carry0[0];
  assign carry_select[2] = carry0[1];
endmodule

module simple_adder_4bit(a, b, cin, sum, cout);
  input [3:0] a, b;
  input cin;
  output [3:0] sum;
  output cout;

  // Logic to compute sum and carry-out
  assign {cout, sum} = a + b + cin;
endmodule

module mux2to1(in0, in1, sel, out);
  input [3:0] in0, in1;
  input sel;
  output [3:0] out;

  // Mux logic
  assign out = sel ? in1 : in0;
endmodule