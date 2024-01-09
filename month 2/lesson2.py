#ООП, наследования, полиморфизм

class Hum: #супер класс - класс, ни от кого не наследуется
    def __init__(self, name):
        self.name = name
        # self.age = age

    def Hi(self):
        ...

    def __str__(self):
        return 'HI'

    def __len__(self):
        return len(self)

h = Hum('fdsf')
h.name = 'rus'
h.Hi()

#Наследование
class Student(Hum):     #дочерний класс - наследутеся
    def Hi(self):
        print('Hello', self.name)

student = Student('rus')
student.Hi()

print(Student.mro())
class Kid(Student):

    def __init__(self, name , age):
        super().__init__(name)
        self.age = age

    def Hi(self):
        Hum.Hi(self)

c = Kid('beka', 14)

c.Hi()

class Kid2(Kid):
    def __init__(self, name, age, lastname, fly=False):
        super().__init__(name, age)
        self.lastname = lastname
        self.fly = fly


    def __str__(self):
        return f"{super().__str__()}, name: {self.name}, age: {self.age}, latname: {self.lastname}, can fly: {self.fly}"

Kid=Kid2('beka', 11, 'wer', False)

print(Kid)

