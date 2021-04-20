# class Deposit:
#     def __init__(self, initial, interest, n):
#         self.initial = initial
#         self.interest = interest
#         self.n = n
#
#     def profit(self):
#         result = int(self.initial * ((1 + self.interest) ** self.n))
#         return result
#
#
# money = Deposit(1000000, 0.035, 7)
# print(money.profit(), '만원')

class Deposit:
    def __init__(self):
        self.initial = 1000000
        self.interest = 0.035
        self.n = 7

    def profit(self):
        result = int(self.initial * ((1 + self.interest) ** self.n))
        return result

money = Deposit()
print(money.initial)