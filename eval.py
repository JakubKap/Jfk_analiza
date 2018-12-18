#!/usr/bin/env python
import antlr4
from gen.WymierneLexer import *
from gen.WymierneParser import *
from frac import *
import sys
import math

def evaluate_further(tree):
    return int(tree.getText())

def evaluate_mult(tree):

    sign = 1
    result = 1

    for child in tree.getChildren():

        text = child.getText()

        if text == '*':
            sign = 1
        elif text == ':':
            sign = -1
        elif text == '%':
            sign = 2
        elif text == 'cong':
            sign = 3
        else:
            if sign == 2:
                result = result % evaluate_further(child)
            elif sign == 3:
                result = math.floor(result / evaluate_further(child))
            else:
                result *= evaluate_further(child) ** sign

    return result



def evaluate(tree):

    def gen_values():

        sign = 1
        for child in tree.getChildren():

            text = child.getText()

            if text == '+':
                sign = 1
            elif text == '-':
                sign = -1
            else:
                yield sign * evaluate_mult(child)

    return sum(gen_values())



if __name__ == '__main__':

    while True:

        try:

            data = input("> ")
            lexer = WymierneLexer(antlr4.InputStream(data))
            tokens = antlr4.CommonTokenStream(lexer)
            parser = WymierneParser(tokens)
            tree = parser.expression()
            print(evaluate(tree))

        except EOFError:
            print("\nZnak EOF, koniec pracy")
            sys.exit(0)
        except KeyboardInterrupt:
            print("\nPrzerwanie ^C, koniec pracy")
            sys.exit(0)

