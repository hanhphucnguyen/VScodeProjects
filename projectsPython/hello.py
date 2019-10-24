# import platform
# a: int = 9
# print('this is version {}'.format(platform.python_version()))
# print('lalala {}'.format(a))

def main():  
    a= dict(a=1,b=2)
    b= [1,2,3,4,5]
    # kitten(**a)
    for i in inclusive_range(4):
        print(i)

def kitten(**b):   
    for i in b:
        print(f'{i}  {b[i]}')

if __name__ == "__main__":
    main()