class A:
    def feacture1(self):
        print('fecture 1 working')

    def feacture2(self):
        print('feacture 2 working')
class B:

    def feacture3(self):
        print('feacture 3 working')

    def feacture4(self):
        print('feacture 4 working')
class C(A,B):
    def feacture5(self):
        print('feacture 5 working')
c1=C()
c1.feacture1()
c1.feacture2()
c1.feacture3()
c1.feacture4()
c1.feacture5()
