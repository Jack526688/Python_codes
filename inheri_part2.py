class A:

    def __init__(self):
        print('init in A')

    def feacture1(self):
        print('fecture 1-A working')

    def feacture2(self):
        print('feacture 2-A working')
class B:

    def __init__(self):
        super().__init__()
        print('init in B ')

    def feacture1(self):
        print('feacture 1-B working')

    def feacture2(self):
        print('feacture 2-B working')

class C(A, B):
    def __init__(self):
        super().__init__()
        print('init in C')

    def fect(self):
        super().feacture2()

a1 = C()

a1.fect()