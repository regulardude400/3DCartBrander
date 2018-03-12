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
cx\_Freeze (only if compiling, is installed via the command below in the Compiling Section.)

Installing pypiwin32
```
Use pip3 install pypiwin32
```

# Compiling
If you would like to compile this program, you can use Cx_Freeze located here:https://anthony-tuininga.github.io/cx_Freeze/

or by running in command prompt:
```
python -m pip install cx\_Freeze --upgrade
```
You would complile via the command prompt in the appropiate directory:
```
python setup.py build
```
It should then output the build directory in the root of the program.
The exe would be located in {ROOT}/build/exe.win32-3.x/

# Running the Program
Run the 3DCartBrander.py or 3DCartBrander.exe
