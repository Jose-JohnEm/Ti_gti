import os
import platform

def os_is_not_compatible(osys):
    if osys == "Windows":
        return False
    elif osys == "Darwin":
        return False
    elif osys == "Linux":
        return False
    return True

def exit_error(err):
    errs = ["", "Sorry gti only works on Windows, Linux, and Mac os",
            "Install failed because some files are missing. Please redownload the module",
            ""]
    for i in range(1, len(errs)):
        if i == err:
            print(errs[i])
    exit(err)

def install_pip(osys):
    if osys == "Windows":
        sh = os.environ['SHELL']
        print(sh)
        #ret = os.system("cd setupsss/ > null")
        #os.system("del /f null")
        #if ret != 0:
        #    exit_error(2)
        #ret = os.system("python get-pip.py")
        return
    else:
        return


def main():
    osys = platform.system()

    if os_is_not_compatible(osys):
        exit_error(1)
    install_pip(osys)
    print("Sucess !")


if __name__ == "__main__":
    main()