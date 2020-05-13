import os
import sys
import platform
import shutil
from tkinter import filedialog

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
            "Unknown shell. Please set cmd.exe as your default shell",
            "Pip installation failed... Make sure you have Internet connection",
            "Pyinstaller installation Failed... Make sure you have Internet connection",
            "Gti compilation failed... Please redownload the module",
            ""]
    for i in range(1, len(errs)):
        if i == err:
            print(errs[i])
    exit(err)

def configure_pip_on_windows():
    sh = os.environ['COMSPEC']
    if sh.find("cmd.exe") == 0:
        exit_error(3)
    ret = os.system("cd setup\ > null")
    os.system("del /f null")
    if ret != 0:
        exit_error(2)
    ret = os.system("cd .\setup\ && python get-pip.py > null")
    os.system("del /f .\setup\\null")
    if ret != 0:
        exit_error(4)
    print("Pip has been correctly installed ! [1/4]")

def configure_pip_on_linux_and_mac():
    pass

def install_pip(osys):
    if osys == "Windows":
        configure_pip_on_windows()
    else:
        configure_pip_on_linux_and_mac()

def install_pyinstaller(osys):
    ret = os.system("pip install pyinstaller --quiet")
    if ret != 0:
        exit_error(5)
    if osys == "Windows":
        os.system("del /f .\\null")
    else:
        os.system("rm -f null")
    print("Pyinstaller has been correctly installed ! [2/4]")

def pyinstall():
    ret = os.system("pyinstaller --onefile gti.py --name gti")
    if ret != 0:
        exit_error(6)
    shutil.rmtree('build', ignore_errors=True)

def move_binaries_windows():
    print("A window opened. Choose Gti location...")
    path = (filedialog.askdirectory() + "\jose-git").replace("\\", "")
    print("Now gti location is : " + path)
    os.mkdir(path)
    shutil.move("dist/gti.exe", path)
    return path.replace("\\", "")

def install_gti(osys):
    pyinstall()
    if osys == "Windows":
        path = move_binaries_windows()
    else:
        pass
    shutil.rmtree('dist', ignore_errors=True)
    os.remove('gti.spec')
    print("Gti has been correctly installed ! [3/4]")
    return path

def add_path(path):
    path = path.replace("/", "\\")
    os.system("setx path \\\"%%path%;" + path +'\"')
    print("setx path \"%path%;" + path +'\"')
    print(os.environ['PATH'])
    print("Gti path has been added to env ! [4/4]")

def main():
    osys = platform.system()

    if os_is_not_compatible(osys):
        exit_error(1)
    install_pip(osys)
    install_pyinstaller(osys)
    path = install_gti(osys)
    if osys != "Windows":
        add_path(path)
    print("Gti is ready for use. Enjoy !")


if __name__ == "__main__":
    main()