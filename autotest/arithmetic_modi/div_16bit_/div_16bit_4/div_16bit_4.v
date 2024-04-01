
module div_16bit(
    input wire [15:0] A,
    input wire [15:0] B,
    output reg [15:0] result,
    output reg [15:0] odd
);
    
    reg [31:0] dividend;
    reg [15:0] divisor;
    reg [15:0] quotient;
    reg [15:0] remainder;
    reg [15:0] temp_dividend;
    integer i;
    
    always @(A or B) begin
        // Preset the values before starting division
        dividend = {16'b0, A};  // Zero-extend A to 32 bits
        divisor = B;
        quotient = 16'b0;
        remainder = 16'b0;

        // Division algorithm starts here
        for (i=15; i>=0; i=i-1) begin
            remainder = remainder << 1;          // Shift remainder to the left
            remainder[0] = dividend[31];         // Take the highest bit from the dividend
            dividend = dividend << 1;            // Shift the dividend to get the next bit
            
            if (remainder >= divisor) begin
                remainder = remainder - divisor;
                quotient[i] = 1;
            end
        end
        
        // Assign the outputs
        result = quotient;
        odd = remainder;
    end

endmodule