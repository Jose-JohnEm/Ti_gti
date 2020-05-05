def is_print(line):
    if line[:6] != "print(" or line[len(line) - 1] != ')':
        return False
    return True

def write_print(line):
    result = "Disp " + line[6:-1]
    return result
