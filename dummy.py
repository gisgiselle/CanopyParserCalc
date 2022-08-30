import calculator
import calculator

grammar = """"

prog <- (expr NEWLINE*)
expression <- addition / factor
addition <- factor (_ "+" _factor)+
substract <- factor (_ "-" _factor)+
division <- factor (_ "/" _factor)+
multiplication <- factor (_ "*" _factor)+

factor <- number / par_expression
number <- "0" / [1-9] [0-9]*
par_expression <- "(" expression ")"
"""
tree = calculator.parse(grammar, "2+1")

for node in tree.elements:
    print (node.offset, node.text)


