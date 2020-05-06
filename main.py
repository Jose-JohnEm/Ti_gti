#!/usr/bin/env python

from sys import argv as av

from src.check_extension import ext_file
from src.check_extension import check_ext

from src.var_affect import str_to_tab
from src.var_affect import is_affectation
from src.var_affect import write_affect

from src.print_disp import is_print
from src.print_disp import write_print

from src.pause import is_pause
from src.pause import write_pause

from src.condition_if import is_an_if
from src.condition_if import is_an_else
from src.condition_if import write_an_if
from src.condition_if import write_an_else

from src.while_loop import is_while
from src.while_loop import write_while

indent = 0
on_if = False

def desindent(line, nb):
    global indent
    global on_if
    tab = 0
    i = 0
    while line[i] == ' ':
        tab += 1
        i += 1
    if indent < tab:
        print("Error : There's bad identation Line " + str(nb + 1))
        exit(1)
    if indent > tab and line.find("else") == -1:
        end = ""
        while indent > tab:
            indent -= 4
            end += "End "
            on_if = False
        return end + line[tab:].strip()
    line = line[tab:]
    return line.strip()


def gti_translator(content):
    global indent
    global on_if
    lines = str_to_tab(content)
    export = ""

    for i in range(0, len(lines)):
        lines[i] = desindent(lines[i], i)
        while lines[i][0:4] == "End ":
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
            indent += 4
            on_if = True
        elif is_an_else(lines[i], on_if):
            export += write_an_else(lines[i])
            on_if = False
        elif is_while(lines[i]) == True:
            export += write_while(lines[i])
            indent += 4
        else:
            print(lines[i])
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