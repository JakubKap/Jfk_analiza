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
NextLine: '\n;
Return: '\r';

Blank: (Space | Tab | NextLine | Return)+ -> skip;

number: (IntNum | FloatNum);

classic_op: (Add | Sub | Mul | Div);
polish_op_mult: (Min | Max);
polish_op_una: (Pow | Sqrt | Neg);

operation: 

    (((number | operation) | (LeftBracket + (number | operation) RightBracket))
    + classic_op +
    ((number | operation) | (LeftBracket + (number | operation) RightBracket))) | 

    (polish_op_mult + LeftBracket + 
        ((number | operation) | (LeftBracket + (number | operation) RightBracket))
    + (Comma + number)* + RightBracket ) |

    (polish_op_una + LeftBracket +
        ((number | operation) | (LeftBracket + (number | operation) RightBracket))
    + RightBracket)
    ;

expression: (operation | numer)
// 2 + (7 + 9) * 4 * (23 + 5)
