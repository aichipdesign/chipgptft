
module accu (
    input clk,
    input rst_n,
    input [7:0] data_in,
    input valid_a,
    output ready_a,
    input ready_b,
    output reg valid_b,
    output reg [9:0] data_out
);

reg [1:0] count; // counter to keep track of the received data
reg [9:0] acc; // accumulator for the inputs
wire end_cnt; // indicates when the counter has reached 4 inputs

assign end_cnt = (count == 2'd3);
assign ready_a = !end_cnt || (end_cnt && ready_b && valid_b); //Ready when not ended or both downstream ready and output valid.

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        count <= 2'd0;
        acc <= 10'd0;
        valid_b <= 1'b0;
        data_out <= 10'd0;
    end else begin
        if (valid_a && ready_a) begin
            acc <= acc + data_in; // accumulate the input data
            if (end_cnt) begin
                data_out <= acc + data_in; // send the result on the 4th data
                acc <= 8'd0; //reset the accumulator
                valid_b <= 1'b1; // assert valid_b on the 4th piece of data
                count <= 2'd0; // reset the counter
            end else begin
                count <= count + 2'd1; // increment the counter
                valid_b <= 1'b0; // de-assert valid_b if it is not the 4th data
            end
        end else if (ready_b && valid_b) begin
            valid_b <= 1'b0; // de-assert valid_b once the downstream module is ready to accept the data
        end
    end
end

endmodule