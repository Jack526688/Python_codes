from abc import ABC, abstractmethod
class Computer:
    @abstractmethod
    def process(self):
        pass

com1 = Computer()

com1.process()