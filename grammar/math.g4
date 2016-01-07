grammar math;

expression
: number
| number operator number
| expression operator expression
| '(' expression ')'
;

number: NUMBER+;

operator: OPERATOR;

NUMBER: '0'..'9';

OPERATOR: '+' | '-' | '*' | '/';


