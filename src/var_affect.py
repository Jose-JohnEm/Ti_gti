def str_to_tab(content):
    lines = []
    x = 0
    nb = 0
    i = 0
    while i < len(content):
        if content[i] == '\n' and (i - x) > 1:
            lines.append(content[x:i])
            x = i + 1
            nb += 1
        i += 1
    lines.append(content[x:i])
    return lines

def valid_affect(char):
    if char.isalnum:
        return True
    elif char == '+' or char == '-' or char == '/' or char == '*':
        return True
    return False

def is_affectation(line):
    if line[0].isalpha == False:
        return False
    step = 1
    for i in range(1, len(line)):
        if step == 1:
            if line[i] == '=':
                step = 2
                continue
            elif line[i] != ' ' and line[i] != '\t':
                return False
        if step == 2:
            if line[i] != ' ' and line[i] != '\t' \
                and valid_affect(line[i]) == False:
                return False
    return True

def write_affect(line):
    export = ""
    for i in range(0, len(line)):
        if line[i] == ' ':
            continue
        if line[i] == '=':
            export += '\u2192'
        else:
            export += line[i]
    export = export[2:len(export)] + export[1] + export[0]
    return export
