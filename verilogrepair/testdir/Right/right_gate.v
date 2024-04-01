module Decoder (d0, d1, d2, d3, d4, d5, d6, d7, x, y, z);
    input x, y, z;
    output d0, d1, d2, d3, d4, d5, d6, d7;

    wire x0, y0, z0;

    not(x0, x);
    not(y0, y);
    not(z0, z);

    and(d0, x0, y0, z0);
    and(d1, x0, y0, z);
    and(d2, x0, y, z0);
    and(d3, x0, y, z);
    and(d4, x, y0, z0);
    and(d5, x, y0, z);
    and(d6, x, y, z0);
    and(d7, x, y, z);

endmodule // Decoder
