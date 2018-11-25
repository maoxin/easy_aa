class People(object):
    def __init__(self, name):
        self.name = name
        self.paid = 0
    def pay(self, money):
        self.paid += money
