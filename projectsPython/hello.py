# import platform
# a: int = 9
# print('this is version {}'.format(platform.python_version()))
# print('lalala {}'.format(a))

def main():  
    a= dict(a=1,b=2)
    kitten(**a)

def kitten(**b):   
    for i in b:
        print(f'{i}  {b[i]}')

if __name__ == "__main__":
    main()