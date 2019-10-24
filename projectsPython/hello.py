# import platform
# a: int = 9
# print('this is version {}'.format(platform.python_version()))
# print('lalala {}'.format(a))

def main():  
    f3()
    
def f(ff):
    def wrap():
        print('this is before f') 
        ff()
        print('this is after f')
    return wrap

@f
def f3():
    print('this is f3')

if __name__ == "__main__":
    main()
  