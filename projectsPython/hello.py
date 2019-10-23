# import platform
# a: int = 9
# print('this is version {}'.format(platform.python_version()))
# print('lalala {}'.format(a))

def main():
    x=5
    kitten(x)
    print(f'x now have value: {x}')

def kitten(a):
    a=3
    print(a)

if __name__ == "__main__":
    main()