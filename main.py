#!/usr/bin/env python

from sys import argv as av
from src.check_extension import ext_file
from src.check_extension import check_ext

from src.var_affect import str_to_tab
from src.var_affect import is_affectation
from src.var_affect import write_affect

indent = 0

def is_print(line):
    if line[:6] != "print(" or line[len(line) - 1] != ')':
        return False
    return True

def write_print(line):
    result = "Disp " + line[6:-1]
    return result

def is_pause(line):
    if line == "pause":
        return True
    return False

def write_pause(line):
    return "Pause "

def is_an_if(line):
    if line[0:4] == "if (" and line[-1] == ')':
        return True
    return False

def write_an_if(line):
    global indent
    result = "If " + line[4:-1].replace(" ", "")
    result += ":Then "
    indent += 4
    return result

def desindent(line, nb):
    global indent
    tab = 0
    i = 0
    while line[i] == ' ':
        tab += 1
        i += 1
    if indent < tab:
        print("Error : There's bad identation Line " + str(nb))
        exit(1)
    if indent > tab:
        indent -= 4
        return "End " + line[tab:].strip()
    line = line[tab:]
    return line.strip()


def gti_translator(content):
    lines = str_to_tab(content)
    export = ""

    for i in range(0, len(lines)):
        lines[i] = desindent(lines[i], i)
        if lines[i][0:4] == "End ":
            export += "End \n"
            lines[i] = lines[i][4:]
        if is_affectation(lines[i]) == True:
            export += write_affect(lines[i])
        elif is_print(lines[i]) == True:
            export += write_print(lines[i])
        elif is_pause(lines[i]) == True:
            export += write_pause(lines[i])
        elif is_an_if(lines[i]) == True:
            export += write_an_if(lines[i])
        else:
            print("Error line " + str(i + 1))
            exit(1)
        export += '\n'
    return export


def main(file):
    source_file = open(file, "r")
    compiled_file = open(file[0:-3] + ".8xp", "w+", encoding="utf-8")
    result = gti_translator(source_file.read())
    compiled_file.write(result)

if __name__ == "__main__":
    if len(av) == 2 and check_ext(ext_file(av[1])) == True:
        main(av[1])