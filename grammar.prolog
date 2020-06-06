%	Gramatica
%
%	<expr> ::= <op> <number> <number>
%	<op> ::= '-' | '+' | '/' | '*'
%	<number> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
%
%	ejemplo
%	+ 1 2
%
%	Defina en prolog un predicado que permita validar la gramatica
%	Anterior
%
%	expr("+",1,2).
%	true.
%
%	expr("+",11,2). % falso por que esta limitado a un solo number
%	false.
%
%	expr("/",10,5).
%	true.
%
%	expr("+","*",2).
%	false.
%
%	Hay un predicado en prolog que te verifica si un atomo es un number
%	number(2).
%	true.
%
%	number('+').
%	false
%
%       INTEGRANTES
% ESQUIVEL MACIAS ERICK XAVIER  16590461
% GÓMEZ OLVERA JACOB MISAEL     16590474

op1('-').
op2('+').
op3('/').
op4('*').
number1(0).
number2(1).
number3(2).
number4(3).
number5(4).
number6(5).
number7(6).
number8(7).
number9(8).
number10(9).

operador(A) :- op1(A); op2(A); op3(A); op4(A).
numero(B)   :- number1(B); number2(B); number3(B); number4(B); number5(B); number6(B); number7(B); number8(B); number9(B); number10(B).
expr(A,B,C) :- operador(A), numero(B), numero(C).
