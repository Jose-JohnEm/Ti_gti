def revstr(str):
    result = []
    i = len(str) - 1
    while i >= 0:
        result.append(str[i])
        i -= 1
    return result

def check_ext(ext):
    if len(ext) == 2 and ext[0] == 't' and ext[1] == 'i':
        return True
    return False

def ext_file(file):
    i = len(file) - 1
    ext = []
    while i >= 0 and file[i] != '.':
        ext.append(file[i])
        i -= 1
    return revstr(ext)