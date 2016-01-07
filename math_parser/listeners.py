from math_parser.grammar.mathListener import mathListener
from antlr4.error.ErrorListener import ErrorListener


class ValidatingListener(mathListener):

    def __init__(self):
        self.characters = set('0123456789+-*/')

    def is_valid(self):
        return not self.characters

    def exitNumber(self, ctx):
        number = ctx.getText()
        if number not in self.characters:
            raise Exception("I don't believe that {} is in {}".format(number, self.characters))
        self.characters.remove(number)

    def exitOperator(self, ctx):
        operator = ctx.getText()
        if operator not in self.characters:
            raise Exception("I don't believe that {} is in {}".format(number, self.characters))
        self.characters.remove(operator)

class BailErrorListener(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(msg)

