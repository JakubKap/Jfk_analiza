grammar Wymierne;

Add: '+';
Sub: '-';
Mul: '*';
Div: ':';
Pow: '^';
Mod: '%';
Cong: 'cong';
Sqrt: 'sqrt';
Neg: 'neg';
Abs: 'abs';
Floor: 'floor';
Ceil: 'ceil';
Round: 'round';
Min: 'min';
Max: 'max';
IntNum: ('0' | [1-9] + [0-9]*); //licznik ułamka lub liczba całkowita np. 4/1
Denominator: ([1-9] + [0-9]*); //mianownik ułamka
FractionBar: '/'; //kreska ułamowa
Fraction: IntNum FractionBar Denominator; //ułamek
Point: '.';
LeftBracket: '(';
RightBracket: ')';
Comma: ',';

fragment Space: ' ';
fragment Tab: '\t';
fragment NextLine: '\n';
fragment Return: '\r';

Blank: (Space | Tab | NextLine | Return)+ -> skip;

number: (IntNum | Fraction);

classic_op: ( Add | Sub | Mul | Div | Mod | Cong);
polish_op_mult: (Min | Max);
polish_op_una: (Sqrt | Neg | Abs | Floor | Ceil | Round);
pow_op: Pow;

expression:
    classic_expression |
    safe_expression |
    pow_expression |
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
    (safe_expression | pow_expression )
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

pow_expression:
    safe_expression
    pow_op
    IntNum
;

//((2))
