# import platform
# a: int = 9
# print('this is version {}'.format(platform.python_version()))
# print('lalala {}'.format(a))
class Car:
    serial = 1234;
    model = 1990
    def showInfo(self,a,b):
        print(f'{self.serial}  {a} {b} {self.model}')

def main():  
    car = Car()
    car.showInfo()


if __name__ == "__main__":
    main()
  