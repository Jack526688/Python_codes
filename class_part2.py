class Computer:
    def __init__(self):
        self.name="kunal"
        self.age=28

    def update(self):
        self.age=30

    def compare(self,other):

        if self.age==other.age:
            return True
        else:
            return False
c1=Computer()
c2=Computer()

c1.age=30

if c1.compare(c2):
    print("the are same")
else:
    print("they are different")

print(c1.name)