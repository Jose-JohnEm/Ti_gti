echo Syntax: asm [NAME (w/o extension)] [PATH]

@echo off
echo ----- Assembling %1 for the TI-83 Plus...
echo #define TI83P >temp.z80
if exist %1.z80 type %1.z80 >>temp.z80
if exist %1.asm type %1.asm >>temp.z80
tasm -80 -i -b -l temp.z80 %1.bin %1.xlt
if errorlevel 1 goto ERRORS
devpac8x %1
copy %1.8xp %1.8xp >nul
del temp.z80 >nul
del %1.bin >nul
del %1.8lt
del %1.xlt
exit
:ERRORS
echo ----- There were errors.
del %1.bin >nul
del %1.8lt
del temp.z80 >nul
exit