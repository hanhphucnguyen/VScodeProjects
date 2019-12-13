def taumBday(b, w, bc, wc, z):
    if (bc == wc or bc+z == wc or wc+z==bc or z>=abs(bc-wc)):
        return b*bc + w*wc
    else:
        if bc>wc:
            return (b+w)*wc + b*z
        else:
            return (b+w)*bc + w*z

def cipher(s,k):
    num = ord(s)
    if 97 <= num <= 122:
        return chr(((num-97+k)%26)+97)
    elif 65 <= num <= 90:
        return chr(((num-65+k)%26)+65)
    else: return s

def main():
    # print(taumBday(3,3,1,9,2))
    print('f')


if __name__ == "__main__":
    main()
