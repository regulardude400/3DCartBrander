import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "3DCartBrander",
        version = "0.8",
        description = "3DCartBrander",
        options = {"build_exe": build_exe_options},
		url='https://github.com/regulardude400/3DCartBrander',
        executables = [Executable("3DCartBrander.py", base=base)])
