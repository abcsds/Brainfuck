import sys
orig = ('>','<','+','-','.',',','[',']') # Origital set of instructions
new  = ('→','←','↑','↓','↘','↙','↗','↖') # New set of instructions

### Verify input
if len(sys.argv) != 3:
    print('''Usage:
    python3 bf.py <input.bf> <output.bf>''')
    sys.exit(0)

inFile  = sys.argv[1]
outFile = sys.argv[2]
with open(inFile, 'r') as codeFile:
    codeSource=list(codeFile.read().replace('\n', '')) # Read input file
source = []
for i in codeSource:
    if i in orig:
        source.append(i)                               # Read input code

dest = []                                              # Init output code
for i in source:
    dest.append(new[orig.index(i)])

with open(outFile, 'w') as codeFile:
    try:
        codeFile.write(''.join(dest))
    except Exception as e:
        raise
