class Calculator:
    # def __init__(self, n, m, func):
    #     self.n = n
    #     self.m = m
    #     self.func = func

    def calc(self, n, m, func):
        self.n = n
        self.m = m
        self.func = func

        if self.func == 'add':
            return Calculator.add(self)
        elif self.func == 'sub':
            return Calculator.sub(self)
        elif self.func == 'mul':
            return Calculator.mul(self)
        elif self.func == 'div':
            return Calculator.div(self)

    def add(self):
        return self.n + self.m

    def sub(self):
        return self.n - self.m

    def mul(self):
        return self.n * self.m

    def div(self):
        return self.n / self.m

while True:
    res = Calculator()
    a = int(input('첫번째 수를 입력하세요 : '))
    b = int(input('두번째 수를 입력하세요 : '))
    word = input('문자열을 입력하세요(add, sub, mul, div) : ')
    print(res.calc(a, b, word))
