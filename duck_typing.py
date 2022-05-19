class Pycharm:
    def execute(self):
        print('compiling')
        print('running')

class Laptop:
    def code(self, ide):
        ide.execute()

a = Pycharm()

lap1=Laptop()
lap1.code(a)