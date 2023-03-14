class Fruits:
    def __init__(self, type, color, price):
        self.mytype = type
        self.mycolor = color
        self.myprice = price

    def onyesha(self):
        print(self.mytype, self.mycolor, self.myprice)


# creating an object
myobj = Fruits("Banana", "Yellow", 20)
myobj.onyesha()
oobj = Fruits("Mango", "Yellow", 60)
oobj.onyesha()


class Employees:
    def __init__(self, employee, field, salary):
        self.myemployee = employee
        self.myfield = field
        self.mysalary = salary

    def onyesha(self):
        print(self.myemployee, self.myfield, self.mysalary)


# object
obj = Employees("Angela" + " ", "a doctor" + " " + "earns a salary of" + "ksh", 60000)
obj.onyesha()
jet = Employees("Cynthia" + " ", "a bank manager" + " " + "earns a salary of" + "ksh", 100000)
jet.onyesha()
bjet = Employees("Kerry" + " ", "an auditor" + " " + "earns a salary of" + "ksh", 250000)
bjet.onyesha()

