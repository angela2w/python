class Person:
    def __init__(self, name, age):
        self.myname = name
        self.myage = age

    def habari(self):
        print("Hello, My name is " + self.myname)


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.mystudent = student_id
        self.myage = age

    def habari(self):
        super().habari()
        print("Im a student with an ID" + str(self.mystudent) + " and im" + str(self.myage))


myname = Student("Angela", 18, 1270899)
myname.habari()


class Mtu:
    def __init__(self, gender, location):
        self.mygender = gender
        self.mylocation = location

    def neno(self):
        print("The following" + " " + self.mygender)


class Mwanafunzi(Mtu):
    def __init__(self, gender, location, employment):
        super().__init__(gender, location)
        self.myemployment = employment
        self.mylocation=location

    def neno(self):
        super().neno()
        print("I am a" + str(self.myemployment) +" " + "in" + " " + str(self.mylocation))


mygender = Mwanafunzi("female", "Nairobi","doctor")
mygender.neno()
