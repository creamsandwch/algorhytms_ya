import sys


line = sys.stdin.readline()
a, b = map(int, str(line).split())
sys.stdout.write(str(a + b))
