from thinkbayes import *


class Bowl:

    def __init__(self, **kw):
        self.cookies = {}
        for name, count in kw.items():
            self.cookies[name] = count

    def PercentOf(self, name):
        if name in self.cookies:
            total = sum(self.cookies.values())
            return self.cookies[name] / float(total)
        else:
            return 0

    def Takeout(self, name):
        if name in self.cookies:
            self.cookies[name] -= 1


class Cookie(Pmf):
    bowls = {
        'Bowl 1': Bowl(vanilla=30, chocolate=10),
        'Bowl 2': Bowl(vanilla=20, chocolate=20)
    }

    def __init__(self, hypos):
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()

    def Update(self, data):
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            print hypo, self.d[hypo], like
            self.Mult(hypo, like)
            self.bowls[hypo].Takeout(data)
        self.Normalize()

    def Likelihood(self, data, hypo):
        bowl = self.bowls[hypo]
        like = bowl.PercentOf(data)
        return like

hypos = ['Bowl 1', 'Bowl 2']
pmf = Cookie(hypos)
dataset = ['vanilla', 'chocolate']
for data in dataset:
    pmf.Update(data)
for hypo, prob in pmf.Items():
    print hypo, prob