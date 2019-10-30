# import platform
# a: int = 9
# print('this is version {}'.format(platform.python_version()))
# print('lalala {}'.format(a))
import sys

class test:
    a:int
 
    def __init__(self, *args):
        self.a= args[0]
        self.b = args[1]

def main():
   
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