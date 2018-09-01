def limitLines(text, COLUMN):
    """
        (string, int) -> string[]
        Returns an array of strings that have at max size COLUMN
    """
    text = text.split()
    lines = []
    line = ''
    for word in text:
        while len(word) > COLUMN - 2:
            lines.append(word[:COLUMN-2])
            word = word[COLUMN-2:]

        if len(word) + len(line) + 1 < COLUMN-2:
            line += word + ' '
        else:
            lines.append(line.strip())
            line = word
    lines.append(line.strip())
    return lines


def blockLine():
    return '+' + '-'*78 + '+'


def center(text):
    """ 
        string -> string
        Takes in a 0-78 sized text and returns the text centerd to 80
    """
    i = int((78 - len(text)) / 2)
    if len(text) % 2 == 0:
        return '|' + ' '*i + text + ' '*i + '|'
    else:
        return '|' + ' '*(i+1) + text + ' '*i + '|'


def entry(text):
    lines = limitLines(text, 73)
    output = '| -> ' + lines[0] + ' '*(74-len(lines[0]))+'|\n'
    for line in lines[1:]:
        output += '|    ' + line + ' '*(74-len(line))+'|\n'

    return output[:-1]


def subtitle(text):
    lines = limitLines(text, 72)
    output = ''
    for line in lines[:-1]:
        output += '|      ' + line.upper() + ' '*(72-len(line)) + '|\n'
    output += '|      ' + lines[-1].upper() + ':' + \
        ' '*(71-len(lines[-1])) + '|'
    return output


def content(text):
    lines = limitLines(text, 70)
    output = ''
    for line in lines:
        output += '|        ' + line + ' '*(70-len(line)) + '|\n'
    return output[:-1]


def title(text):
    """ returns a box with a centered title """
    lines = limitLines(text, 78)
    output = blockLine() + '\n'
    for line in lines:
        output += center(line) + '\n'
    return output + blockLine()


def br():
    return '|' + ' '*78 + '|'