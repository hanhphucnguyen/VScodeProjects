# import platform
# a: int = 9
# print('this is version {}'.format(platform.python_version()))
# print('lalala {}'.format(a))
# import sys

import student
# from datetime import date
# from datetime import time
# from datetime import datetime
# from datetime import timedelta
import os
from os import path
import shutil

    
class test(student.Student):
    def __init__(self, *args):
        super().__init__(*args)
    def bark(self):
        print(f'{self.name} bark bark')

def testf(x):
    print("big" if x>7 else "small")
    c = 9 if x>7 else 0
    print(c)

class testAgr:
    def __init__(self, *args):
        if len(args)==3:
            self.result = 3
        elif len(args)==2:
            self.result = 2
        elif len(args)==1:
            self.result = 1

class sub(testAgr):
    def __init__(self, *args):
        super().__init__(*args)
def main():
    # src = path.realpath('hello.py')
    # print(f'the real path : {src}')
    # des = src + '.bak'
    # shutil.copy(src,des)
    # print(os.name)
    # print(path.realpath('hello.py'))
    # print(timedelta(10,5,5))
    # now = datetime.now()
    # print(now)
    # testf(8)
    # a = testAgr(1,2,3)
    # b= testAgr(1,2)
    # c= testAgr(1)
    # print(f'{a.result}  {b.result}  {c.result}')
    # a = sub(1,2,3)
    # b= sub(1,2)
    # c= sub(1)
    # print(f'{a.result}  {b.result}  {c.result}')
    # for i,j in enumerate(arr):
    #     if i>2: break
    #     print("sort" if arr[i]<arr[i+1] else "not sort")
    # print(student.x)
    # a = test('phuc',35)
    # print(f'name : {a.name} Age: {a.age}')
    # a.bark()
    # b= student.Student('phuc','35')
    # b.bark()
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
    