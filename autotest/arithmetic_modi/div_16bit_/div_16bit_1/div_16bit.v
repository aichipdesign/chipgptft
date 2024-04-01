
module div_16bit(
    input wire clk,
    input wire reset,
    input wire start,
    input wire [15:0] A, // Dividend
    input wire [15:0] B, // Divisor
    output reg [15:0] result, // Quotient
    output reg [15:0] odd // Remainder
);

// Internal signals
reg [15:0] dividend, divisor;
reg [15:0] accumulator;
reg [4:0] count; // 16 cycles for division
reg [2:0] state;
wire borrow;
wire [15:0] subtracted;

// States
localparam S0 = 0,
           S1 = 1,
           S2 = 2,
           S3 = 3;

assign subtracted = accumulator - divisor;
assign borrow = (accumulator < divisor);

always @(posedge clk or posedge reset) begin
    if (reset) begin
        state <= S0;
        result <= 16'd0;
        odd <= 16'd0;
        dividend <= 16'd0;
        divisor <= 16'd0;
        accumulator <= 16'd0;
        count <= 5'd0;
    end else begin
        case (state)
            S0: begin
                // Load the dividend and divisor, and initialize the count
                if (start) begin
                    dividend <= A;
                    divisor <= B;
                    accumulator <= 16'd0;
                    result <= 16'd0;
                    odd <= 16'd0;
                    count <= 16'd0;
                    state <= S1;
                end
            end
            S1: begin
                // Compare and shift
                if (count < 16) begin
                    // Left align the divisor with the current part of the dividend
                    accumulator[15:0] <= {accumulator[14:0], dividend[15]};
                    dividend <= dividend << 1;
                    state <= S2;
                end else begin
                    state <= S3;
                end
            end
            S2: begin
                // Subtract if no borrow, otherwise just shift
                if (!borrow) begin
                    accumulator <= subtracted;
                    result[count] <= 1'b1;
                end
                count <= count + 1;
                state <= S1;
            end
            S3: begin
                // Finish division, output the result
                odd <= accumulator;
                state <= S0; // Return to idle state
            end
        endcase
    end
end

endmodule