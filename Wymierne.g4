grammar Wymierne;

Add: '+';
Sub: '-';
Mul: '*';
Div: '/';
Pow: '^';
Sqrt: 'sqrt';
Neg: 'neg';
Min: 'min';
Max: 'max';
IntNum: ('0' | [1-9] + [0-9]*);
Point: '.';
LeftBracket: '(';
RightBracket: ')';
Comma: ',';
FloatNum: IntNum Point IntNum;

Space: ' ';
Tab: '\t';
NextLine: '\n';
Return: '\r';

Blank: (Space | Tab | NextLine | Return)+ -> skip;

number: (IntNum | FloatNum);

classic_op: (Add | Sub | Mul | Div);
polish_op_mult: (Min | Max);
polish_op_una: (Pow | Sqrt | Neg);

expression:
    classic_expression |
    safe_expression |
    LeftBracket
    expression
    RightBracket
    ;

safe_expression:
    polish_mult_expression |
    polish_una_expression |
    number
;

classic_expression:
    safe_expression
     classic_op
    expression
;

polish_mult_expression:
    polish_op_mult LeftBracket
        expression
    (Comma expression)*  RightBracket
;

polish_una_expression:
    polish_op_una LeftBracket
        expression
    RightBracket
;

//((2))