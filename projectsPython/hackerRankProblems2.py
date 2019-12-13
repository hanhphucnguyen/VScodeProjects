def taumBday(b, w, bc, wc, z):
    if (bc == wc or bc+z == wc or wc+z==bc or z>=abs(bc-wc)):
        return b*bc + w*wc
    else:
        if bc>wc:
            return (b+w)*wc + b*z
        else:
            return (b+w)*bc + w*z

def caesarCipher(s,k):
    result=''
    for i in s:
        num = ord(i)
        if 97 <= num <= 122:
            i = chr(((num-97+k)%26)+97)
        elif 65 <= num <= 90:
            i= chr(((num-65+k)%26)+65)
        result += i
    return result
    

def main():
    # print(taumBday(3,3,1,9,2))
    print(caesarCipher('middle-Outz',2))


if __name__ == "__main__":
    main()
