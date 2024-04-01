
module accu(
    input            clk,
    input            rst_n,
    input      [7:0] data_in,
    input            valid_a,
    input            ready_b,
    output           ready_a,
    output reg       valid_b,
    output reg [9:0] data_out
);

// Internal signals
reg [9:0] accumulator;
reg [1:0] counter;

assign ready_a = (counter < 4) ? ready_b : 1'b0; // Only ready if less than 4 items are accumulated

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        // Reset state
        accumulator <= 0;
        counter <= 0;
        data_out <= 0;
        valid_b <= 0;
    end else begin
        // Handshaking mechanism
        if (valid_a && ready_a) begin
            // Accumulate input data
            accumulator <= accumulator + data_in;
            counter <= counter + 1;

            // Prepare to output if 4 data items have been accumulated
            if (counter == 3) begin
                // Ready to send output
                data_out <= accumulator + data_in; // Include the current data item
                valid_b <= 1'b1;
            end else begin
                valid_b <= 1'b0;
            end
        end else begin
            if (ready_b && valid_b) begin
                // Once data is accepted by downstream, reset for next accumulation
                accumulator <= 0;
                counter <= 0;
                valid_b <= 1'b0;
            end
        end
    end
end

endmodule