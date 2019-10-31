# import platform
# a: int = 9
# print('this is version {}'.format(platform.python_version()))
# print('lalala {}'.format(a))
# import sys
from student import Student


class test(Student):
    def __init__(self, *args):
        super().__init__(*args)
    def bark(self):
        print(f'{self.name} bark bark')
x=10
def main():
    # a = test('phuc',35)
    # print(f'name : {a.name} Age: {a.age}')
    # a.bark()
    global x
    x += 1
    print(x)
    # for i in range(len(l)):
    #     if (i>0 and l[i-1]==l[i]):
    #         continue
    #     else: 
    #         print(f'{l[i]} appear {l.count(l[i])}')
   
    # p= open('text.txt', 'rt')
    # q = open('textcopy.txt', 'wt')
    # for i in p:
    #     q.writelines(i)
    # while True:
    #     buffer = p.read(500)
    #     if buffer: q.write(buffer)
    #     else: break

if __name__ == "__main__":
    main()
    print(x)