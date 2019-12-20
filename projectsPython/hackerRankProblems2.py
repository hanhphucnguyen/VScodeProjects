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

def marsExploration(s):
    count = 0
    i=0
    while i < len(s):
        for j in 'SOS':           
            if s[i] != j:
                count +=1
            i +=1  
    return count

def hackerrankInString(s):
    sample = 'hackerrank'
    cur = 0
    for i in s:
        if i == sample[cur]:
            cur +=1
        if cur>= len(sample): break

    if cur >= len(sample):
        return 'YES'
    else:
        return 'NO'

def pangrams(s):
    sample = 'abcdefghijklmnopqrstuvwxyz '
    sampleDic = dict.fromkeys(sample,0)
    s = s.lower()
    for i in s:
        sampleDic[i] +=1
    flag = True
    for i in sample:
        if i == ' ':pass
        else:
            if sampleDic[i]<1:
                flag = False
                break
    if flag: 
        return 'pangram'
    else:
        return 'not pangram'


def main():
    # print(taumBday(3,3,1,9,2))
    # print(caesarCipher('middle-Outz',2))
    # print(marsExploration('SOSSRT'))
    # print(hackerrankInString('hackerworld'))
    # print(pangrams('Wepromptlyjudgedantiqueivorybucklesforthenprize'))

    i = {'o':1,'j':7}
    for n,m in i.items():
        print(m)


if __name__ == "__main__":
    main()
