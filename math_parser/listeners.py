from math_parser.grammar.mathListener import mathListener
from antlr4.error.ErrorListener import ErrorListener


class ValidatingListener(mathListener):

    def __init__(self):
        self.characters = set('0123456789+-*/')

    def is_valid(self):
        return not self.characters

    def exitNumber(self, ctx):
        for number in ctx.getText():
            self.parse(number)

    def exitOperator(self, ctx):
        operator = ctx.getText()
        self.parse(operator)

    def parse(self, character):
        if character not in self.characters:
            raise Exception("I don't believe that {} is in {}".format(character, self.characters))
        self.characters.remove(character)

class BailErrorListener(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(msg)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise Exception(msg)

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise Exception(msg)

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise Exception(msg)
