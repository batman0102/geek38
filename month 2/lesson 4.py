#множественное наседование
#venv - модули, библиотеки, зависимости, фреймворки, пакеты

class Hum:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(self.name, 'run')

hum1 = Hum('albus')
hum1.run()


class Hum3(Hum):
    pass





class SuperHum:
    def __init__(self, name, superpower):
        self.name = name
        self.power= superpower

    def run(self):
        print(self.power)

c = SuperHum('albus', 'Mage')

class Hum2(Hum3, Hum, SuperHum):
    def run(self):
        Hum.run(self)
        SuperHum.run(self)


h=Hum2('name1')
h.power = 'RAVE'
h.name = 'q'
h.run()
#MRO - method resoltion order(порядок выполнения методов)

print(Hum2.mro())






