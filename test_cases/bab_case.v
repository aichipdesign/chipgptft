module BlockMEM(config_clk, config_reset, config_out, config_in, reset, clk, in0, in1, out0);
	parameter size = 32;

	input config_clk, config_reset, config_in, reset, clk;
	output config_out;
	input [size-1:0] in0, in1;
	output [size-1:0] out0;

	wire config_sig_0;
	wire [size-1:0] in0;
	wire [size-1:0] in1;
	wire [size-1:0] MEM0_out0;

	config_cell #1 config_cell_0(
		.config_clk(config_clk),
		.config_reset(config_reset),
		.config_in(config_in),
		.config_out(config_out),
		.config_sig(config_sig_0)
	);

	MEM MEM0(
		.clk(clk),
		.reset(reset),
		.config_sig(config_sig_0),
		.in0(in0),
		.in1(in1),
		.out0(MEM0_out0)
	);

	assign out0 = MEM0_out0;


endmodule