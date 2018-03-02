import re, os
import win32com.client as win32
#Global variables to be used to generate the email text.

Gemail = ""

Gtransid = ""

Gusername = ""

Gcontrolp = ""

Gusernamep = ""

Gpasswordp = ""

Ghostftp = ""

Gloginftp = ""

Gpassftp = ""

def parseEmail():
        try:
                with open("3dcart_info_Goes_Here.txt", 'r') as file:
                    for i, lines in enumerate(file):
                             
                        #transaction center id credentials
                        transid = re.search(r'TranCenter', lines)
                        if transid:
                            global Gtransid
                            Gtransid = lines[18:]

                        #email
                        emailTo = re.search(r'Email address for merchant is', lines)
                        if emailTo:
                             global Gemail
                             Gemail = lines[31:]
                             
                        username = re.search(r'User Name', lines)
                        if username:
                            global Gusername
                            Gusername = lines[14:]
                            
                        #control panel 3d cart credentials
                        controlp = re.search(r'Your control panel:', lines)
                        if controlp:
                            global Gcontrolp
                            Gcontrolp = lines[21:]
                            
                        usernamep = re.search(r'Your username:', lines)
                        if usernamep:
                            global Gusernamep
                            Gusernamep = lines[16:]
                            
                        passwordp = re.search(r'Your password:', lines)
                        if passwordp:
                            global Gpasswordp
                            Gpasswordp = lines[16:]
                        
                        #ftp settings
                        hostftp = re.search(r'com\.3dcartstores\.com', lines)
                        if ((hostftp) and i in range(50,58)):
                            global Ghostftp
                            Ghostftp = lines[:-2]
                            
                        loginftp = re.search(r'\|', lines)
                        if loginftp:
                            global Gloginftp
                            Gloginftp = lines[7:-2]
                            
                        passftp = re.search(r'Password:', lines)
                        if passftp and i in range(55,60):
                            global Gpassftp
                            Gpassftp = lines[10:-2]

                file.close()
        except IOError:
                file = open("3dcart_info_Goes_Here.txt", 'w')
                file.write("\\DELETE ME WITH 3DCart INFO FROM EMAIL IN OUTLOOK")
                print("Please paste the 3D cart information in the file 3dcart_info.txt. "
                      "This file has been created for you in the same directory "
                      "where you ran the script or program.\n")
                input('Press ENTER to exit')
                exit()
                
def createEmail():
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = Gemail
        mail.Subject = "Replace this text."
        text = "Replace this text."
        mail.Body = text
        if mail.Display(False):
           mail.Display(True)

def makeScpScript():
        text2write = "open \"ftps://" + Gloginftp + ':' + Gpassftp +'@'+ Ghostftp + '\"\n'
        text2write += 'cd /keys\n'
        text2write += 'put "C:\\KEY_YOU_WANT_TO_COPY.ids\n"'
        text2write += 'put "C:\\KEY_YOU_WANT_TO_COPY.ids1\n"'
        text2write += 'cd ../web/assets\n'
        text2write += 'put "C:\\Folder_OR_FILE_YOU_WANT_TO_COPY.txt\n"'
        text2write += "exit"
        with open("scpScript.txt", 'w') as scpfile:
            scpfile.write(text2write)
            scpfile.close()
            
        dirScpFile = os.path.realpath(scpfile.name)
        return '"' + dirScpFile + '"'
                    
def sendftp():
        port = 990
        result = makeScpScript()
        command = "winscp.com /script=" + result
        os.system("start cmd /k " + command)
        
if __name__ == "__main__":
    parseEmail()
    createEmail()
    sendftp()
