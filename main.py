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

def desindent(line, nb):
    tab = 0
    i = 0
    while line[i] == '\t':
        tab += 1
    if indent != tab:
        print("Error : There's bad identation Line " + str(nb))
        exit(1)
    line = line[tab:len(line)]
    return line.strip()

def gti_translator(content):
    lines = str_to_tab(content)
    export = ""

    for i in range(0, len(lines)):
        lines[i] = desindent(lines[i], i)
        if is_affectation(lines[i]) == True:
            export += write_affect(lines[i])
        elif is_print(lines[i]) == True:
            export += write_print(lines[i])
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