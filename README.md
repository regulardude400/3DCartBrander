# 3DCartBrander
This program was made to parse emails that come in from 3D cart and provide you with a way to easily parse the email and copy files to 3dcart via WinSCP program.

# Requirements:

Windows Programs:

Outlook version 2003 or higher.(This is used to automatically compose an email using win32com from the pypiwin32 python library)
https://products.office.com/en-us/outlook/email-and-calendar-software-microsoft-outlook?tab=tabs-1

WinSCP (Any version that supports calling and executing scripts.)

Note:
(Do a custom installation and make sure it is installed to the environment path or python will complain winscp.com doesn't exist).

Download:
https://winscp.net/eng/download.php

# Python Internal and External Libraries Needed:

__Internal__
os
re (regular expressions)

__External__
_These libraries are installed typically via pip or pip3._

pypiwin32 is installed via the command below.
Pyinstaller (only if compiling, is installed via the command below in the Compiling Section.)

Installing pypiwin32
```
Use pip3 install pypiwin32
```

# Compiling
If you would like to compile this program, you can use PyInstaller located here:https://www.pyinstaller.org/

or by running in command prompt:
```
pip install pyinstaller
```
Be sure to edit the spec file that comes with the download in the root directory.

You need to edit line 7 where it says: "pathex=['C:\\PATH\\TO\\FOLDER\\THAT\\CONTAINS\\3DCartBrander.PY'],"

Change this path to a real path where to the __folder__ that contains 3DCartBrander.py.

Do not put the exact path to the 3DCartBrander.py as line 6 already knows which file to compile.


You would complile via running Compile.bat or the command prompt in the appropiate directory:
```
pyinstaller --clean 3DCartBrander.spec
```

It should then output the build directory in the root of the program.
The exe would be located in {ROOT}/dist/3DCartBrander.exe
The gui file that qt5 creates is located also in the same folder as the exe. (Don't delete the ui file.)

# Running the Program
Run the 3DCartBrander.py or 3DCartBrander.exe with the appropiate dialog.ui in the same directory.
