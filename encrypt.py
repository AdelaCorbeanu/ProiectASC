# python encrypt.py input.txt key output
import sys
f = open(sys.argv[1])
s = f.read()
characters = [ord(x) for x in s]
f.close()

key = [ord(x) for x in sys.argv[2]]

f = open(sys.argv[3], "w")
cnt = 0
length = len(key)
for ch in characters:
    f.write(chr(ch ^ key[cnt]))
    cnt += 1
    if cnt == length:
        cnt = 0
f.close()
