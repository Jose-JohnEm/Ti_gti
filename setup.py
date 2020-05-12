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
    if err == 1:
        print("Sorry gti only works on Windows, Linux, and Mac os")
    exit(err)

def install_pip(osys):
    pass

def main():
    osys = platform.system()

    if os_is_not_compatible(osys):
        exit_error(1)
    install_pip(osys)
    print("Sucess !")


if __name__ == "__main__":
    main()