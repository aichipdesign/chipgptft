module counter (clk, rst, en, count);  

   input clk, rst, en;
   output reg [1:0] count;

   assign en = count | clk;
always @(posedge clk)
      if (rst)
         count <= 2'd0;
      else if (en)
         count <= count + 2'd1;

	wire our_d, our_e;
	assign our_d = count && rst;
	assign our_e = clk || our_d;
	assign rst = our_e;
endmodule

