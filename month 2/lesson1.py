# ООП
# class и все его внутренности
#
# p = 'str', 1, 1.4, True, {}, [], (), None
# print(type(p))
#
# def a(b,k):
#     print(b+k)
# a(3, 9)
# a(2, 8)
# a(9, 9)

# 1 правило - названия писать с большой буквы

class Human:
    # свойство class - переменная, записанная внутри class
    head = '11'
    #магический метод - метод, только у него два нижних подчеркивания в начале и в конце
    #str - отвечает только за print
    def __str__(self):
        return f'{self.head} name: {self.name}, age: {self.age}, nickname: {self.nick}, abilka: {self.power}'

    def __len__(self):
        return len(self.power)
    #init - отвечает за аргументы в скобках (конструктор класса)
    def __init__(self, name, age, nickname, abilka):
        self.name = name
        self.age = age
        self.nick = nickname
        self.power = abilka
    # Любая функция внтури class - метод
    def Hi(self):
        print(self.age * 2)
# Переменная, созданная на основе класса - экземпляр или объект
hum = Human('beka', 20, 'T9','писать стихи')
hum2 = Human('Ибрагим', 14, 'kuizee', 'играть')
hum3 = Human('Руслан', 16, 'rave', "играть на гитаре")
print(len(hum))
hum2.RT = 'Расширение территории'
hum.age = 10
print(hum.age)
print(hum2.RT)
hum.Hi()

class Human2:
    def __init__(self, name, age, nickname, abilka):
        self.name = name
        self.age = age
        self.nick = nickname
        self.power = abilka

    def hello(self):
        self.name = 'vondf'
Human2.hello(hum)

print(hum)





# git, github, gitlub



