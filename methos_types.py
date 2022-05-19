class Student:
    collage = "DPU uni"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def ave(self):
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):
        return self.m1

    @classmethod
    def info(cls):
        return cls.collage

    @staticmethod
    def static():
        print('this is static method')


s1 = Student(55, 66, 77)
s2 = Student(44, 55, 88)

# print(s1.ave())

print(Student.info())
print(s2.get_m1())

Student.static()