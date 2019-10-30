# import platform
# a: int = 9
# print('this is version {}'.format(platform.python_version()))
# print('lalala {}'.format(a))
def main():

    l = [1,1,1,2,3,4,4]
    l.reverse()
    print(l) 
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