""" Parse math expression """

import sys

from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker, BailErrorStrategy
from math_parser.grammar.mathLexer import mathLexer
from math_parser.grammar.mathParser import mathParser
from math_parser.listeners import ValidatingListener, BailErrorListener

def main(argv):
    """ Parse the argument as a math expression """

    data = InputStream(argv[1])
    lexer = mathLexer(data)
    lexer.addErrorListener(BailErrorListener())

    stream = CommonTokenStream(lexer)

    parser = mathParser(stream)
    parser._errHandler = BailErrorStrategy()

    tree = parser.expression()
    listener = ValidatingListener()
    walker = ParseTreeWalker()

    walker.walk(listener, tree)

    if listener.is_valid():
        print "I like that expression"
    else:
        print "You forgot about {}".format(listener.characters)

if __name__ == '__main__':
    main(sys.argv)
