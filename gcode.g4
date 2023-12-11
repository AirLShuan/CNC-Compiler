grammar gcode;

start : expr | <EOF> ;

expr     : 'G00' x_cord=NUMBER y_cord=NUMBER #nodrawExpr
         | 'G01' x_cord=NUMBER y_cord=NUMBER #drawlineExpr
         | 'G02' x_cord=NUMBER y_cord=NUMBER radius=NUMBER #drawccExpr
         | 'G03' x_cord=NUMBER y_cord=NUMBER radius=NUMBER #drawcccExpr
         | 'print' x_cord=NUMBER y_cord=NUMBER #printlineExpr
         ;
NUMBER : ('0' .. '9') + ('.' ('0' .. '9') +)? ;
WS : [ \r\n\t]+ -> skip;