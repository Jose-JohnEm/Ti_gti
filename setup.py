import os
import sys
import platform
import shutil

if platform.system() == "Windows":
    from tkinter import filedialog


def exit_error(err):
    errs = ["", "Sorry gti only works on Windows, Linux, and Mac os",
            "Install failed because some files are missing. Please redownload the module",
            "Unknown shell. Please set cmd.exe as your default shell",
            "Pip installation failed... Make sure you have Internet connection",
            "Pyinstaller installation Failed... Make sure you have Internet connection",
            "Gti compilation failed... Please redownload the module",
            "Gti installation failed... Because you don't give SUDO rights.\nRestart with sudo !",
            ""]
    for i in range(1, len(errs)):
        if i == err:
            print(errs[i])
    exit(err)


def os_is_not_compatible(osys):
    if osys == "Windows":
        return False
    elif osys == "Darwin":
        return False
    elif osys == "Linux":
        return False
    return True


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
    #-----LINUX AND DARWIN INSTALLATION-----#
    ret = os.system("cd setup/ > null && rm -f null")
    if ret != 0:
        exit_error(2)
    ret = os.system("cd setup && python3 get-pip.py > null && rm -f null")
    if ret != 0:
        exit_error(4)
    print("Pip has been correctly installed ! [1/4]")
    

def install_pip(osys):
    if osys == "Windows":
        configure_pip_on_windows()
    else:
        configure_pip_on_linux_and_mac()


def install_pyinstaller(osys):
    ret = os.system("pip install pyinstaller --quiet")
    if ret != 0:
        exit_error(5)
    print("Pyinstaller has been correctly installed ! [2/4]")


def pyinstall(osys):
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

def move_binaries_darlin():
    path = "/usr/local/bin/jose-git"
    if os.system("ls " + path) != 0:
        try:
            os.system("sudo mkdir " + path)
        except ValueError:
            exit_error(7)
    os.system("sudo mv dist/gti " + path)
    return path

def install_gti(osys):
    pyinstall(osys)
    if osys == "Windows":
        path = move_binaries_windows()
    else:
        path = move_binaries_darlin()
    shutil.rmtree('dist', ignore_errors=True)
    os.remove('gti.spec')
    print("Gti has been correctly installed ! [3/4]")
    return path


def add_path(path, osys):
    if osys == "Linux":
        os.system("echo 'export PATH=$PATH:/usr/local/bin/jose-git' >> ~/." +
        os.environ["SHELL"][os.environ["SHELL"].rfind("/") + 1:] + "rc")
        print("Just set $PATH variable within gti location [4/4]\n")
    print("Gti has been added !\n\nGti is ready for use !")
    if osys == "Windows":
        print("You need to add gti path on the environnement [4/4]\n\n \
            Run :    setx path\"%path%;" + path)


def main():
    osys = platform.system()

    #print(os.environ["SHELL"][os.environ["SHELL"].rfind("/") + 1:])
    #exit(0)
    if os_is_not_compatible(osys):
        exit_error(1)
    install_pip(osys)
    install_pyinstaller(osys)
    path = install_gti(osys)
    add_path(path, osys)
    print("Enjoy !")


if __name__ == "__main__":
    main()