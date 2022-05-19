class A:
    def show(self):
        print('apple')


class B(A):
    def show(self):
        print('realme')


a1 = B()
a1.show()
