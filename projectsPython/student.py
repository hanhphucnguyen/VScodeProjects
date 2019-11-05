class Student:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
    def bark(self):
        print('student bark')
x=10