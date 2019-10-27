# import platform
# a: int = 9
# print('this is version {}'.format(platform.python_version()))
# print('lalala {}'.format(a))
def main():
    print('hello world')
    p= open('text.txt', 'rt')
    q = open('textcopy.txt', 'wt')
    # for i in p:
    #     q.writelines(i)
    while True:
        buffer = p.read(500)
        if buffer: q.write(buffer)
        else: break

if __name__ == "__main__":
    main()