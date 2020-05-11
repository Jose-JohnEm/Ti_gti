from .condition_if import is_a_test
from .condition_if import operator_replace
from .var_affect import is_affectation

def is_while(line):
    if line[:7] == "while (" and line[-1] == ')':
        if is_a_test(line[7:-1]):
            return True
    return False

def write_while(line):
    result = "While " + line[7:-1].replace(" ", "")
    result = operator_replace(result)
    return result

def is_do_while(line):
    if line[:10] == "do while (" and line[-1] == ')':
        if is_a_test(line[10:-1]):
            return True
    return False

def write_do_while(line):
    result = "Repeat " + line[10:-1].replace(" ", "")
    result = operator_replace(result)
    return result

def is_a_for_test(exp):
    exp = exp.replace(" ", "")
    if is_affectation(exp[:exp.find(";")]) == False:
        return False
    if exp[exp.find(";") + 1:exp.rfind(";")].isnumeric() == False:
        return False
    if exp[exp.rfind(";") + 1:].isnumeric() == False:
        return False
    return True

def is_for(line):
    if line[:5] == "for (" and line[-1] == ')':
        if is_a_for_test(line[5:-1].replace(" ", "")):
            return True
    return False

def write_for(line):
    line = line[5:-1].replace(" ", "")
    result = "For(" + line[:line.find(";")].replace("=", ",")
    result += line[line.find(";"):].replace(";", ",") + ')'
    result = operator_replace(result)
    return result