#инкапсуляция - капсула - сборка чего-либо в единое целое

from lesson2 import Hum

# h=Hum('name')
# h.Hi()

#уровни доступа: публичный(public), защищенный(protected), скрытый(private)


from lesson2 import Hum
class Person(object):
    def __init__(self,firstname,lastname,age,money):
        self.first=firstname
        self.last=lastname
        self._age=age
        self.__money=money
    def __str__(self):
        return self.first

    def HI(self):
        print(f'Hi my name is {self.first} {self.last}\n'
              f'my old {self._age}')
    @property
    def money(self):
        print(self.__money)
    def cash(self, atr):
        self.__money=atr


first=Person('beka','qwerty',20,2020)
# first.first='Бека'
# first._age=10000
# first._Person__money = 0 #name manling
# first.age2=22
# print(first,first.age2)
# first.HI()
# first.cash()
# # print(dir(first))
# first.set_cash(20)
# first.get_money(30)




# class P2(Person):
#
#     # def st(self):
#     #     return super().__str()
#
#     def str(self):
#         return f' hi {super().str()}'
#


# p=P2('first')
# print(p)
# print(p.st())