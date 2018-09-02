import txtFormatter
import sys

def loadFile():
    s = ''
    with open(sys.argv[1] + '.txt') as f:
        s = f.readlines()
    return s

def doLine(f, line):
    line = line.split()
    command = line[0]
    input = ' '.join(line[1:])

    if command == 'title':
        f.write(txtFormatter.title(input))
    elif command == 'break':
        f.write(txtFormatter.br())
    elif command == 'block':
        f.write(txtFormatter.blockLine())
    elif command == 'entry':
        f.write(txtFormatter.entry(input))
    elif command == 'subtitle':
        f.write(txtFormatter.subtitle(input))
    elif command == 'content':
        f.write(txtFormatter.content(input))
    else:
        f.close()
        raise SyntaxError(str(command) +  'does not exist.')
    f.write('\n')


filename = sys.argv[1]
toWrite = open(filename + '_out.txt', 'w')
read = loadFile()
for line in read:
    doLine(toWrite, line)
toWrite.close()