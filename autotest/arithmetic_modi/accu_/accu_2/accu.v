
module accu (
    input         clk,
    input         rst_n,
    input [7:0]   data_in,
    input         valid_a,
    output        ready_a,
    input         ready_b,
    output reg    valid_b,
    output reg [9:0] data_out
);

// Register and wire declarations
reg [9:0] accumulator;
reg [1:0] count;
wire      end_cnt; // Indicates when 4 cycles are completed

assign end_cnt = (count == 3);
assign ready_a = valid_b && ready_b; // Upstream can only send data if downstream is ready to accept data

// Counter logic
always @(posedge clk or negedge rst_n) begin
    if (!rst_n)
        count <= 2'b0;
    else if (valid_a && ready_a)
        count <= (count == 3) ? 2'b0 : count + 1;
end

// Accumulator logic
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        accumulator <= 10'b0;
        valid_b <= 0;
        data_out <= 0;
    end else if (valid_a && ready_a) begin
        accumulator <= accumulator + data_in; // Accumulate data
        // Generate valid_b signal
        valid_b <= end_cnt; // Valid only when the last data of the batch is received
        if (end_cnt) begin
            data_out <= accumulator + data_in; // Output accumulation after 4 inputs
            accumulator <= 10'b0; // Reset accumulator for the next batch
        end
    end
end

endmodule