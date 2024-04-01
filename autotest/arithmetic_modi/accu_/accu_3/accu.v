
module accu(
    input        clk,
    input        rst_n,
    input [7:0]  data_in,
    input        valid_a,
    output       ready_a,
    input        ready_b,
    output reg   valid_b,
    output reg [9:0] data_out
);

reg [1:0] count;
reg [9:0] sum;
wire end_cnt;
assign end_cnt = count == 2'b11; // Indicates the completion of four data inputs.

assign ready_a = (count < 2'b11) || (count == 2'b11 && ready_b && !valid_b); // Ready for new data if count is not full or if downstream is ready and valid_b is low.

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        count <= 2'b0;
        sum <= 10'b0;
        valid_b <= 1'b0;
        data_out <= 10'b0;
    end else begin
        // Handle valid new input
        if (valid_a && ready_a) begin
            sum <= sum + data_in; // Accumulate input data
            count <= count + 1'b1;
        end
        
        // Once four inputs are received, prepare data for output and assert valid_b
        if (end_cnt && (!valid_b || (valid_b && ready_b))) begin
            valid_b <= 1'b1;
            data_out <= sum;
        end
        
        // Reset accumulator and count when data is accepted by downstream
        if (valid_b && ready_b) begin
            sum <= 10'b0;
            count <= 2'b0;
            valid_b <= 1'b0; // Dependent on the specific protocol; could remain high until new data comes
        end
    end
end

endmodule