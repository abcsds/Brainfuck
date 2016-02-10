import sys
sym = ('>','<','+','-','.',',','[',']') # Origital set of instructions
inf = sys.argv[1]                       # input file
instr = ' '.join(sys.argv[2:])          # input string

### Verify input
if len(sys.argv) < 2:
    print('''Usage:
    python3 bf.py <Sourcefile.bf> <Program input>''')
    sys.exit(0)

### Initialize brainfuck code
A = [0]                      # Main buffer
n = 0                        # Length of main buffer
ptr = 0                      # Program pointer
loop = []                    # Loop buffer
skipFlag = False             # Flag as loop helper
inBuffer = list(' '.join(sys.argv[2:]))
inBuffer.reverse()

### Read main program into a list of instructions
with open(inf, 'r') as codeFile:
    codeSource=list(codeFile.read().replace('\n', ''))
code = []
for i in codeSource:
    if i in sym:
        code.append(i)
# print(code)
code.append('/0')

while True:
    if skipFlag and code[ptr] != sym[7]:
        if code[ptr] == '/0':
            raise BufferError
            sys.exit(1)
        ptr += 1
        continue
    if code[ptr] == sym[0]:
        ''' Move buffer right one '''
        if len(A) <= n+1:
            A.append(0)
        n+=1
        ptr += 1
    elif code[ptr] == sym[1]:
        ''' Move buffer left one '''
        if n > 0:
            n-=1
        ptr += 1
    elif code[ptr] == sym[2]:
        ''' Add 1 to current buffer '''
        A[n]+=1
        ptr += 1
    elif code[ptr] == sym[3]:
        ''' Substract 1 from current buffer '''
        A[n]-=1
        ptr += 1
    elif code[ptr] == sym[4]:
        ''' Print current buffer '''
        try:
            print(chr(A[n]), end="")
        except ValueError:
            pass
        ptr += 1
    elif code[ptr] == sym[5]:
        ''' Read item from stdin to buffer '''
        try:
            inChar = inBuffer.pop()
            A[n] = int(inChar)
        except ValueError:
            print('''Error reading char''') # TODO: there shouldn't be any ValueError if oly code comes in.
        except IndexError:
            pass
        ptr += 1
    elif code[ptr] == sym[6]:
        ''' Start loop, skip if current buffer is zero '''
        if A[n] != 0:
            loop.append(ptr)
        else:
            skipFlag = True
        ptr += 1
    elif code[ptr] == sym[7]:
        ''' Loop: return to start of loop '''
        try:
            ptr = loop.pop()
        except IndexError:
            ptr += 1
            skipFlag = False # If loop list is empty, continue
    elif code[ptr] == '/0':
        sys.exit(0)
    else:
        ptr += 1
