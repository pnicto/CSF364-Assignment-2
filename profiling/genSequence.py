import random, sys
nucleotides = ['A', 'C', 'G', 'U']
s = ''.join(random.choice(nucleotides) for _ in range(int(sys.argv[1])))
f = open('in.txt', 'w')
f.write(s)
