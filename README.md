# 3DCartBrander
This program was made to parse emails that come in from 3D cart and provide you with a way to easily parse the email and copy files to 3dcart via WinSCP program.

# Requirements:

Windows Programs:
Outlook version 2003 or higher.
WinSCP (Any version that supports calling and executing scripts.)

# Python Internal and External Libraries Needed:

__Internal__
os
re (regular expressions)

__External__
pypiwin32 is installed via the command below.
cx\_Freeze (only if compiling, is installed via the command below in the Compiling Section.)

Installing pypiwin32
```
Use pip3 install pypiwin32
```

# Compiling
If you would like to compile this program, you can use Cx\_Freeze located here:https://anthony-tuininga.github.io/cx_Freeze/

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
