class car:

    wheel=4

    def __init__(self):
        self.mil=20
        self.com="BMW"

c1=car()

car.wheel=6

print(c1.mil, c1.com, c1.wheel)