# import platform
# a: int = 9
# print('this is version {}'.format(platform.python_version()))
# print('lalala {}'.format(a))


class Car:
    def __init__(self, *a):
        self.a = a[0]
        self.b = a[1]
        self.c: int = 9

    def setA(self, a=None):
        if a:
            self.a = a

    def __str__(self):
        return f'this is to string method {self.a} {self.b}'


def main():
    file1 = open('text.txt', 'rt')
    file2 = open('textcopy.txt', 'wt')
    for i in file1:
        file2.writelines(i)
    file2.close()
    print('done')


if __name__ == "__main__":
    main()
