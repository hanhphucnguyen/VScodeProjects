# import platform
# a: int = 9
# print('this is version {}'.format(platform.python_version()))
# print('lalala {}'.format(a))

def main():  
    a= [2,3,4,5,6]
    kitten(*a)

def kitten(*b):   
    for i in b:
        print(i)

if __name__ == "__main__":
    main()