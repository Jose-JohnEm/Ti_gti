

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


def is_an_if(line):
    if line[0:4] != "if (" or line[-1] != ')':
        return False
    if is_a_test(line[4:-1]):
        return True
    
def write_an_if(line):
    result = "If " + line[4:-1].replace(" ", "")
    result = result.replace("==", "=")
    result = result.replace("!=", "≠")
    result = result.replace("<=", "≤")
    result = result.replace(">=", "≥")
    result += ":Then "
    return result