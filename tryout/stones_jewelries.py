import sys
import re

j = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()

count = 0

for letter in s:
    if letter in j and re.match('[a-zA-Z]', letter):
        count += 1

sys.stdout.write(str(count))
