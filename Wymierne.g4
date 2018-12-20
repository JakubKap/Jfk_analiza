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
FractionBar: '/'; //kreska ułamowa
Fraction: IntNum FractionBar  ('+' | '-')? IntNum; //ułamek
Point: '.';
LeftBracket: '(';
RightBracket: ')';
Comma: ',';

fragment Space: ' ';
fragment Tab: '\t';
fragment NextLine: '\n';
fragment Return: '\r';

Blank: (Space | Tab | NextLine | Return)+ -> skip;

number:  ('+' | '-')? (IntNum | Fraction);

function: ('+' | '-')? (Min | Max);

pow_operator: Pow;
additive_operator: (Add | Sub);
multiplicative_operator: (Mul | Div | Mod | Cong);
function_single_value: ('+' | '-')? (Sqrt | Neg | Abs | Floor | Ceil | Round );

function_expression:
    function
    LeftBracket expression (Comma expression)*  RightBracket
;

function_single_value_expression:
    function_single_value
    LeftBracket expression RightBracket
;

pow_expression:
    safe_expression
    pow_operator
    IntNum
;

safe_expression:
    function_expression |
    function_single_value_expression |
    number |
    expression_in_brackets
;

secondary_expression:

    safe_expression |
    pow_expression
;

multiplicative_expression:

    secondary_expression
    (
        multiplicative_operator
        secondary_expression
    )*
;

expression:

        multiplicative_expression
        (
            additive_operator
            multiplicative_expression
        )*
;

expression_in_brackets:
    (LeftBracket expression RightBracket)
;


//((2))
