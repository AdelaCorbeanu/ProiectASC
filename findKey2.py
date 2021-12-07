f = open("output.txt")
Output = f.read()
f.close()
string = ""
afisate = 0


def verif():
    for ch in range(a, b):
        for lenKey in range(10, 16):
            for i in range(index, l-1, lenKey):
                x = ord(string[i]) ^ ch
                if (x < 32 or x > 126) and (x != 10):
                    break
            else:
                global afisate
                afisate += 1
                print(chr(ch), end="")
                return 1
    return 0


l = len(Output)//8
for i in range(1, l):
    string += chr(int(Output[(i-1)*8:8*i], 2))
for index in range(0, l, 1):
    a, b = 97, 123
    if verif() == 0:
        a, b = 65, 91
        if verif() == 0:
            a, b = 48, 58
            verif()
    if afisate == 50:
        break
