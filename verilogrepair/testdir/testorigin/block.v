`timescale 1ns / 1ps

module Decoder(
input [2:0] in,
output reg [7:0] out);
always@(*)
begin
case(in)
    3'b000:out=8'b0111_1111;
    3'b001:out=8'b1011_1111;
    3'b010:out=8'b1101_1111;
    3'b011:out=8'b1110_1111;
    3'b100:out=8'b1111_0111;
    3'b101:out=8'b1111_1011;
    3'b110:out=8'b1111_1101;
    3'b111:out=8'b1111_1110;
    default:out=8'b1111_1111;
endcase
end
endmodule