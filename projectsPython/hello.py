# import platform
# a: int = 9
# print('this is version {}'.format(platform.python_version()))
# print('lalala {}'.format(a))

def main():  
    a=dict(lala=1,b=2)
    for i in a.values():
        print(f'{i} ')

    print(a.get('lal'))


if __name__ == "__main__":
    main()
  