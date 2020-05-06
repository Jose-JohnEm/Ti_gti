from .condition_if import is_a_test
from .condition_if import operator_replace

def is_while(line):
    if line[:7] == "while (" and line[-1] == ')':
        if is_a_test(line[7:-1]):
            return True
    return False


def write_while(line):
    result = "While " + line[7:-1].replace(" ", "")
    result = operator_replace(result)
    return result