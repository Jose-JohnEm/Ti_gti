

def is_a_test(line):
    if line.find("==") != -1:
        return True
    if line.find("!=") != -1:
        return True
    if line.find("<") != -1:
        return True
    if line.find(">") != -1:
        return True
    if line.find("<=") != -1:
        return True
    if line.find(">=") != -1:
        return True
    return False

def operator_replace(result):
    result = result.replace("==", "=")
    result = result.replace("!=", "≠")
    result = result.replace("<=", "≤")
    result = result.replace(">=", "≥")
    return result


def is_an_if(line):
    if line[0:4] != "if (" or line[-1] != ')':
        return False
    if is_a_test(line[4:-1]):
        return True
    return False
    
def write_an_if(line):
    result = "If " + line[4:-1].replace(" ", "")
    result = operator_replace(result) + ":Then "
    return result

def is_an_else(line, on_if):
    if line != "else":
        return False
    if on_if == True:
        return True
    return False

def write_an_else(line):
    result = "Else "
    return result