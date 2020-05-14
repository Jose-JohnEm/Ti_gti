# TI_GTI 1.0 Release (non stable)

If you wan't to download the stable version, check out the `stable` branch.

# Ti

This a new programmation language I created.
Its goal its to facilitate Calculator programmation allowing
a best computer programming experience.


# Gti

This is the compilator.
I have to created this because calculators can't understand
my language. So Gti's goal is to translate the Ti code to
calculators code. Then, we just have to copy the rendering
on the calculator.

# How to install

**Before this, make sure that Python is already installed in your computer !**
Then,
There is in the main directory a file named `setup.py`. Run :
$ python setup.py

If you're in Windows, a window will open asking you a location for Ti_Gti binaries.
If you're in Linux, the default location `/usr/local/bin` will be used,
so the programm will ask you your password to get sudo rights to write in.
If you're in Mac, the same thing should happen (*I can't test this in Mac so contact me if a problem occurs*)

When intallation finshed and succeed, restart your shell.
Now you've got Gti command line !

# How to use

## First

Open a text editor and start coding following Ti rules
written on a manual soon

### Then

On a terminal command, type : `python3    main.py    $[your file].ti`
The program only works with .ti files.
Make sure that compilation succed, else an error message
will appear showing you at which line did the compilator failed

### Finally

Open `$[your file].8xp` which is your rendering and just copy this
code to your calculator, then try and enjoy your new program !

# Know this !
- Coded in Python, this last one need to be installed else it will not works.
- Like its name can make you believe, the rendering only works on Ti Calculators.
- Ti is a language which allowing you to code easilier. But, it can't yet debug your code !
- Ti still lack flexibility, so at the slightest syntax error, Gti will not can compile.
- Gti translate from Ti language to alphanumeric calcultor language and not its native (Tasm). That's why you need to copy the rendering manually or using Ti Connect CE
