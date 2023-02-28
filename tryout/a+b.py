line = open('input.txt', mode='r').readline()
a, b = map(int, (str(line).split()))
open('output.txt', mode='w').write(str(a + b))
