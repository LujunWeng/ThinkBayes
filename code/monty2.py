from thinkbayes import *


class Monty(Suite):

    def Likelihood(self, data, hypo):
        if hypo == data:
            return 0
        elif hypo == 'A':
            return 0.5
        else:
            return 1

suite = Monty('ABC')
suite.Update('B')
suite.Print()
