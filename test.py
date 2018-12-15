#!/usr/bin/env python
import antlr4
from gen.WymierneLexer import *
from gen.WymierneListener import *
from gen.WymierneParser import *
import sys


if __name__ == '__main__':

    while True:

        data = input("> ")
        lexer = WymierneLexer(antlr4.InputStream(data))
        tokens = antlr4.CommonTokenStream(lexer)
        parser = WymierneParser(tokens)
        tree = parser.expression()
        print(tree.toStringTree(recog=parser))
