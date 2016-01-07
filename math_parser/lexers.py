from math_parser.grammar.mathLexer import mathLexer


class BailErrorLexer(mathLexer):

    def __init__(self, input):
        super(BailErrorLexer, self).__init__(input)

    def recover(self, re):
        character = self._input.getText(start, stop)
        raise Exception("Unrecognized token encountered: {}".format(self.getErrorDisplay(character)))
