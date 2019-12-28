# import platform
# a: int = 9
# print('this is version {}'.format(platform.python_version()))
# print('lalala {}'.format(a))
# import sys

import student
import collections
from collections import Counter
import math
import random
import time
from enum import Enum
# from datetime import date
# from datetime import time
# from datetime import datetime
# from datetime import timedelta
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile
import urllib.request

    
class test(student.Student):
    def __init__(self, *args):
        super().__init__(*args)
    def bark(self):
        print(f'{self.name} bark bark')
    def __str__(self):
        return "hihi test"

def testf(x):
    print("big" if x>7 else "small")
    c = 9 if x>7 else 0
    print(c)

def abc(x):
    if x%2==0:
        return False
    else:
        return True

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


def decotest(f):
    def run():
        print('before')
        f()
        print('after')
    return run

@decotest
def hehe():
    print('abc')

class Haha(Enum):
    o=1
    u=2

def main():
    
    # enum class
    # print(Haha.o.value)
    
    # date,time,os test 
    # print(os.name)   
    # print(timedelta(10,5,5))
    # now = datetime.now()
    # print(now)

    # class test
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

    # copy content
    # p= open('text.txt', 'rt')
    # q = open('textcopy.txt', 'wt')
    # for i in p:
    #     q.writelines(i)
    # while True:
    #     buffer = p.read(500)
    #     if buffer: q.write(buffer)
    #     else: break

    # sh copy 
    # src = path.realpath('hello.py')
    # print(f'the real path : {src}')
    # des = src + '.bak'
    # shutil.copy(src,des)
    # a,b = path.split(src)
    # print(f'{a}        {b}')
    # make_archive('archive','zip',a)

    # zipfile create
    # with ZipFile('testzip.zip','w') as newzip:
    #     newzip.write('input.txt')
    #     newzip.write('text.txt')
    # newzip = ZipFile('testzip.zip','w')
    # newzip.write('input.txt')
    # newzip.write('text.txt')

    # URL request
    # weburl = urllib.request.urlopen('http://www.google.com')
    # print(f'{weburl.getcode()}')
    # read = weburl.read()
    # print(read)

    # check is instance
    # a = test('phuc',32)
    # print(isinstance(a,student.Student))

    # math & random library
    # print(math.gcd(12,3))
    # for i in range(10):
    #     a = random.randrange(10)
    #     print(a)
    # ar = ['cat','dog','shit']
    # print(random.choice(ar))
    # random.shuffle(ar)
    # a = random.randrange(10,20)
    # print(a)

    # time module
    # i = 0
    # for j in range(10):
    #     time.sleep(1)
    #     print(i)
    #     i+=1

    # decorator test
    # hehe()

    # GeneratorExpession
    # i = 7 if 4>5 else 4
    # a = [str(i) for i in range(10)]
    # print(a)
    # print(type(a))
    # with open('input.txt','rt') as f:
    #     for i in f:
    #         print(i)

    # all and any bool value
    # a = all(i.isdigit() for i in '123a')
    # a = any(i.isdigit() for i in '123a')
    # print(str(a))
       
    # i = (1,2,3,4)
    # z = list(filter(abc,i))
    # print(z)
    # i = [1,2,3,4]
    # j = dict.fromkeys(i,0)
    # print(j)

    # deque datatype
    # u=[1,2,3,4]
    # i = collections.deque(u)
    # print(i)

    # i = {'o':1,'j':7}
    # for n,m in i.items():
    #     print(m)


if __name__ == "__main__":
    main()
   
    