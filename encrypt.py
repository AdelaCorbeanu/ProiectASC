# python encrypt.py input.txt key output
import sys

f = open(sys.argv[1])
Input = f.read()
f.close()

key = sys.argv[2]

f = open(sys.argv[3], "w", encoding="utf-8")
length = len(key)
cnt = 0
for ch in Input:
    f.write(chr(ord(ch) ^ ord(key[cnt])))
    cnt += 1
    if cnt == length:
        cnt = 0
f.close()
