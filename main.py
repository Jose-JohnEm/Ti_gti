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

from src.loops import write_while
from src.loops import write_do_while
from src.loops import write_for
from src.loops import is_while
from src.loops import is_do_while
from src.loops import is_for

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

def check_for_indent_commands(line, tmp):
    if tmp != "":
        return tmp
    global indent
    global on_if
    if is_an_if(line) == True:
        exp = write_an_if(line)
        indent += 4
        on_if = True
    elif is_while(line) == True:
        exp = write_while(line)
        indent += 4
    elif is_do_while(line) == True:
        exp = write_do_while(line)
        indent += 4
    elif is_for(line) == True:
        exp = write_for(line)
        indent += 4
    else:
        exp = ""
    return exp

def check_for_classic_commands(line):
    global on_if
    if is_affectation(line) == True:
        exp = write_affect(line)
    elif is_print(line) == True:
        exp = write_print(line)
    elif is_pause(line) == True:
        exp = write_pause(line)
    elif is_an_else(line, on_if):
        exp = write_an_else(line)
        on_if = False
    else:
        exp = ""
    return exp

def my_error(line, i):
    if line == "":
        print(line)
        print("Error line " + str(i + 1))
        exit(1)


def gti_translator(content):
    global on_if
    lines = str_to_tab(content)
    export = ""
    tmp = ""

    for i in range(0, len(lines)):
        lines[i] = desindent(lines[i], i)
        while lines[i][0:4] == "End ":
            export += "End \n"
            lines[i] = lines[i][4:]
        tmp = check_for_classic_commands(lines[i])
        tmp = check_for_indent_commands(lines[i], tmp)
        my_error(lines[i], i)
        export += tmp + '\n'
    return export


def main(file):
    source_file = open(file, "r")
    compiled_file = open(file[0:-3] + ".8xp", "w+", encoding="utf-8")
    result = gti_translator(source_file.read())
    compiled_file.write(result)

if __name__ == "__main__":
    if len(av) == 2 and check_ext(ext_file(av[1])) == True:
        main(av[1])