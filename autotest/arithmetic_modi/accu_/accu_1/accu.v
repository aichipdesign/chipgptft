
module accu (
    input clk,
    input rst_n,
    input [7:0] data_in,
    input valid_a,
    output reg ready_a,
    input ready_b,
    output reg valid_b,
    output reg [9:0] data_out
);

// State definitions for FSM
localparam WAIT = 1'b0,
           ACCUMULATE = 1'b1;

reg [1:0] count;
reg [9:0] sum;
reg state;

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        // Asynchronous reset
        count <= 2'b00;
        sum <= 10'd0;
        state <= WAIT;
        ready_a <= 1'b0;
        valid_b <= 1'b0;
        data_out <= 10'd0;
    end else begin
        // Default assignments to avoid latches
        ready_a <= 1'b0;
        valid_b <= 1'b0;

        case (state)
            WAIT: begin
                if (valid_a && ready_b) begin
                    // We can accept data and downstream is ready
                    ready_a <= 1'b1;
                    state <= ACCUMULATE;
                    sum <= data_in; // Start the accumulation
                    count <= 1;
                end
            end
            ACCUMULATE: begin
                if (valid_a) begin
                    // Continue accumulating data until we have 4
                    sum <= sum + data_in;
                    count <= count + 1;
                    if (count == 3) begin
                        // We have accumulated 4 data items
                        valid_b <= 1'b1; // Indicate valid output
                        data_out <= sum; // Output the sum
                        if (ready_b) begin
                            // Reset only if downstream is ready to accept the new data
                            count <= 2'b00;
                            sum <= 10'd0;
                            state <= WAIT;
                        end
                    end else begin
                        ready_a <= 1'b1; // Notify ready to accept more data
                    end
                end
            end
        endcase
    end
end

endmodule