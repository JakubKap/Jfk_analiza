#!/usr/bin/env python
import antlr4
from gen.WymierneLexer import *
from gen.WymierneParser import *
import sys

def drawTreeReq(tree, level):

    child_len = sum(1 for _ in tree.getChildren())

    i = 0
    for child in tree.getChildren():

        if not isinstance(child, antlr4.tree.Tree.TerminalNode):

            if child_len == 1:
                print('    ' * level + child.getRuleContext().__class__.__name__[:-7])
                drawTreeReq(child, level)
            else:
                print('    '*level + child.getRuleContext().__class__.__name__[:-7])
                drawTreeReq(child, level+1)
        elif i == 0:
            i += 1
            print('    '*level + tree.getText())

def drawTree(tree):
    drawTreeReq(tree, 0)


if __name__ == '__main__':

    while True:

        try:

            data = input("> ")
            lexer = WymierneLexer(antlr4.InputStream(data))
            tokens = antlr4.CommonTokenStream(lexer)
            parser = WymierneParser(tokens)
            tree = parser.expression()
            drawTree(tree)

        except EOFError:
            print("\nZnak EOF, koniec pracy")
            sys.exit(0)
        except KeyboardInterrupt:
            print("\nPrzerwanie ^C, koniec pracy")
            sys.exit(0)

