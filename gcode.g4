grammar gcode;

start : expr | <EOF> ;

expr     : 'G01' x_cord=NUMBER y_cord=NUMBER #drawlineExpr    
         | 'print' x_cord=NUMBER y_cord=NUMBER #printlineExpr    
         ;
NUMBER : ('0' .. '9') + ('.' ('0' .. '9') +)? ;
WS : [ \r\n\t]+ -> skip;