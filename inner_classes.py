class Student:

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.lap = self.Laptop()

    def show(self):
        print("detail", self.name, self.roll_no)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = 'apple'
            self.model = 'pro_m1'
            self.ram = 16

        def show(self):
            print(self.brand, self.model, self.ram)


s1 = Student('kunal', 5)
s2 = Student('omi', 56)
s2.show()


