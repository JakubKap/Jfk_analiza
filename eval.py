#!/usr/bin/env python
import antlr4
from gen.WymierneLexer import *
from gen.WymierneParser import *
from frac import *
import sys
import math

def evaluate_safe(tree):

    expr_type = tree.getRuleContext().__class__.__name__
    
    if expr_type == 'Function_expressionContext':

        children = tree.getChildren()
        expr_list = []
        iter(children)
        func_name = next(children).getText()
        next(children)
        comma = ','
        while comma == ',':
            expr = next(children)
            expr_list.append(evaluate(expr))
            comma = next(children).getText()

        if func_name == 'min':
            return fmin(expr_list)
        elif func_name == '-min':
            return mfmin(expr_list)
        elif func_name == 'max':
            return fmax(expr_list)
        elif func_name == '-max':
            return mfmax(expr_list)
        
    elif expr_type == 'Function_single_value_expressionContext':

        children = tree.getChildren()
        iter(children)
        func_name = next(children).getText()
        next(children)
        expr = next(children)

        if func_name == 'sqrt':
            return fsqrt(evaluate(expr))
        elif func_name == '-sqrt':
            return fsqrt(evaluate(expr)).negative()
        elif func_name == 'neg':
            return evaluate(expr).negative()
        elif func_name == '-neg':
            return evaluate(expr).norm()
        elif func_name == 'abs':
            return fabs(evaluate(expr))
        elif func_name == '-abs':
            return mfabs(evaluate(expr))
        elif func_name == 'floor':
            return ffloor(evaluate(expr))
        elif func_name == '-floor':
            return ffloor(evaluate(expr)).negative()
        elif func_name == 'ceil':
            return fceil(evaluate(expr))
        elif func_name == '-ceil':
            return fceil(evaluate(expr)).negative()
        elif func_name == 'round':
            return fround(evaluate(expr))
        elif func_name == '-round':
            return fround(evaluate(expr)).negative()

    elif expr_type == 'NumberContext':
        splitted = tree.getText().split('/', 1)
        if len(splitted) == 1:
            return Fraction(int(tree.getText()), 1)
        return Fraction(int(splitted[0]), int(splitted[1]))
    elif expr_type == 'Expression_in_bracketsContext':

        children = tree.getChildren()
        iter(children)
        next(children)
        expr = next(children)
        return evaluate(expr)

    return Fraction(0, 1)


def evaluate_further(tree):

    if tree.getRuleContext().__class__.__name__ == 'Pow_expressionContext':
        children = tree.getChildren()
        iter(children)
        base = next(children)
        next(children)
        expo = next(children)
        return evaluate_safe(next(base.getChildren())) ** int(expo.getText())

    return evaluate_safe(next(tree.getChildren()))

def evaluate_mult(tree):

    sign = 1
    result = f(1, 1)

    for child in tree.getChildren():

        text = child.getText()
        childchild = next(child.getChildren())

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
                result = result % evaluate_further(childchild)
            elif sign == 3:
                result = result // evaluate_further(childchild)
            elif sign == 1:
                result *= evaluate_further(childchild)
            elif sign == -1:
                result *= reversed(evaluate_further(childchild))

    return result



def evaluate(tree):

    result = Fraction(0, 1)
    sign = 1

    for child in tree.getChildren():

        text = child.getText()

        if text == '+':
            sign = 1
        elif text == '-':
            sign = -1
        else:
            if sign == 1:
                result += evaluate_mult(child)
            else:
                result += evaluate_mult(child).negative()

    return result



if __name__ == '__main__':

    while True:

        try:

            data = input("> ")
            lexer = WymierneLexer(antlr4.InputStream(data))
            tokens = antlr4.CommonTokenStream(lexer)
            parser = WymierneParser(tokens)
            tree = parser.expression()
            print(evaluate(tree))

        except AssertionError:
            print("Blad skladni")
        except EOFError:
            print("\nZnak EOF, koniec pracy")
            sys.exit(0)
        except KeyboardInterrupt:
            print("\nPrzerwanie ^C, koniec pracy")
            sys.exit(0)

