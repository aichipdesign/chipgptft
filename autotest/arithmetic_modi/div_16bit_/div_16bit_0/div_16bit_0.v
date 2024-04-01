
module div_16bit(
    input wire clk,              // System clock
    input wire reset,            // Reset signal
    input wire start,            // Start signal for division
    input wire [15:0] A,         // Dividend input
    input wire [15:0] B,         // Divisor input
    output reg [15:0] result,    // Quotient output
    output reg [15:0] remainder, // Remainder output
    output reg done              // Done signal
);

// Define states for FSM
localparam [1:0] IDLE = 2'b00,
                 COMPARE = 2'b01,
                 SHIFT = 2'b10,
                 DONE = 2'b11;

// Internal registers
reg [15:0] acc;
reg [15:0] divisor;
reg [15:0] quotient;
reg [4:0] count;

// Current state and next state registers
reg [1:0] current_state, next_state;

// Combinatorial block for state transition
always @(*) begin
    case (current_state)
        IDLE: 
            next_state = start ? COMPARE : IDLE;
        COMPARE: 
            next_state = SHIFT;
        SHIFT: 
            next_state = (count == 0) ? DONE : COMPARE;
        DONE: 
            next_state = IDLE;
        default: 
            next_state = IDLE;
    endcase
end

// Sequential block for state updates and division algorithm
always @(posedge clk or posedge reset) begin
    if (reset) begin
        current_state <= IDLE;
        acc <= 0;
        divisor <= 0;
        quotient <= 0;
        remainder <= 0;
        count <= 0;
        done <= 0;
    end else begin
        case (current_state)
            IDLE: begin
                if (start) begin
                    acc <= A;
                    divisor <= B;
                    quotient <= 0;
                    remainder <= 0;
                    count <= 15; // Initialize the counter
                    done <= 0;
                end
            end
            COMPARE: begin
                // Compare the upper bits with the divisor
                if (acc >= divisor) begin
                    quotient[15] <= 1;
                    acc <= acc - divisor;
                end
                remainder <= acc; // Save the intermediate remainder
            end
            SHIFT: begin
                quotient <= quotient << 1; // Shift quotient left to make room for the next bit
                acc <= {acc[14:0], A[15-count]}; // Concatenate the remainder with the next bit from the dividend
                count <= count - 1; // Decrement the bit counter
            end
            DONE: begin
                result <= quotient;
                remainder <= acc;
                done <= 1;
            end
        endcase
        if (current_state != IDLE) current_state <= next_state; // Update current state, except when in IDLE
    end
end

endmodule