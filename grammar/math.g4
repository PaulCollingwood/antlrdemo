grammar math;

expression: number ( operator number )+;

number: NUMBER+;

operator: OPERATOR;

NUMBER: '0'..'9';

OPERATOR: '+' | '-' | '*' | '/';
