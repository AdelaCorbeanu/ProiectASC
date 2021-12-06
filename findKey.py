f = open("input.txt")
Input = f.read()
f.close()
f = open("output.txt")
Output = f.read()
f.close()
for i in range(1, 50):
    print(chr(ord(Input[i-1]) ^ int(Output[(i-1)*8:8*i], 2)), end="")
