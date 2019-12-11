def taumBday(b, w, bc, wc, z):
    if (bc == wc or bc+z == wc or wc+z==bc or z>=abs(bc-wc)):
        return b*bc + w*wc
    else:
        pass


def main():
    print(taumBday(5,9,2,3,4))


if __name__ == "__main__":
    main()
