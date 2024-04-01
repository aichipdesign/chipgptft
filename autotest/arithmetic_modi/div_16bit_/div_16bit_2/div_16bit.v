
module div_16bit(
    input wire [15:0] A, // Dividend
    input wire [7:0] B,  // Divisor
    output reg [15:0] result, // Quotient
    output reg [15:0] odd     // Remainder
);

// Internal signals
reg [15:0] dividend;
reg [15:0] divisor;
reg [16:0] remainder; // 1 extra bit to handle subtraction borrow
reg [7:0] count;

// Division algorithm process
always @(A, B) begin
    // Initialization
    dividend = A;
    divisor = {8'b0, B}; // Zero-pad divisor to 16 bits
    remainder = 0;
    result = 0;
    count = 16; // Counter to keep track of iterations

    // Division algorithm
    while (count > 0) begin
        // Left shift remainder, bring in new bit from the dividend
        remainder = {remainder[15:0], dividend[15]};
        dividend = dividend << 1; // Shift dividend for next iteration

        // Compare and subtract
        if (remainder >= divisor) begin
            remainder = remainder - divisor;
            result[count - 1] = 1; // Set quotient bit if subtracted
        end

        count = count - 1;  // Decrement counter
    end

    odd = remainder; // Remaining part is the odd or remainder
end

endmodule