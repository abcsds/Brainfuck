import sys
sym = ('>','<','+','-','.',',','[',']')
inf = sys.argv[1]                       # input file
instr = ' '.join(sys.argv[2:])          # input string

### Verify input
if len(sys.argv) < 2:
    print('''Usage:
    python bf.py <Sourcefile.bf>''')
    sys.exit(0)

### Initialize brainfuck code
A = [0]                      # Main buffer
n = 0                        # Length of main buffer
ptr = 0                      # Program pointer
loop = []                    # Loop buffer
skipFlag = False             # Flag as loop helper

### Read main program into a list of instructions
with open(inf, 'r') as codeFile:
    code=list(codeFile.read().replace('\n', ''))
for i in code:
    if i not in sym:
        # code[i].remove() # TODO
        continue
code.append('/0')

while True:
    if skipFlag and code[ptr] != sym[7]:
        if code[ptr] == '/0':
            raise BufferError
            sys.exit(1)
        ptr += 1
        continue
    if code[ptr] == sym[0]:
        ''' Move buffer up one '''
        if len(A) >= n+1:
            A.append(0)
        n+=1
        ptr += 1
        # print(A[n])
    elif code[ptr] == sym[1]:
        ''' Move buffer down one '''
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
        print(A[n], end="")
        try:
            # sys.stdout.write(chr(A[n]+66))
            print(chr(A[n]), end="")
        except ValueError:
            pass
        ptr += 1
    elif code[ptr] == sym[5]:
        ''' Read item from stdin to buffer '''
        pass # TODO: input disabled for now
    elif code[ptr] == sym[6]:
        ''' Start loop, skip if current buffer is zero '''
        if A[n] != 0:
            loop.append(code.index(i))
        else:
            skipFlag = True
        ptr += 1
    elif code[ptr] == sym[7]:
        ''' Loop: return to start of loop '''
        ptr = loop.pop()
    elif code[ptr] == '/0':
        print()
        print(A)
        sys.exit(0)
    else:
        ptr += 1
