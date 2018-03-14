import sys, re, os, importlib, win32com.client as win32
from gui3DCart import Ui_MainWindow
from PyQt5 import QtWidgets, uic

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

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('dialog.ui', self)
        self.show()
        self.ClearTextBox.clicked.connect(self.clearText) #Clear text
        self.SaveTextToFile.clicked.connect(self.saveText)#Save text to file
        self.StartProgram.clicked.connect(self.runScript) #Runs the main script
        self.actionQuit.triggered.connect(self.quitProgram) #Quits Program
        self.actionAbout.triggered.connect(self.aboutProgram) #Open About in Menu
        
    def aboutProgram(self):
        aboutInfo = QMessageBox()
        aboutInfo.setIcon(QMessageBox.Information)
        aboutInfo.setText("About 3D Cart Brander and Emailer")
        aboutInfo.setInformativeText("This program was created by Alvin Williams."
                                     "If you need help or troubleshooting please report"
                                     "the issues to me in person, via email alvin.williams1992@yahoo.com"
                                     "or via github using the issue tracker located here: https://github.com/regulardude400/3DCartBrander/issues")
    def quitProgram(self):
        sys.exit() #Quit the program
        
    def runScript(self):
        self.parseEmail() #Parse the text file.
        self.createEmail() #Create the email to send and open it in outlook.
        self.sendftp() #Copy the necessary files to the merchant's 3dcart ftp

    def clearText(self):
        self.EmailTextBox.clear() #Clear the 3D Cart Email Text Box
            
    def saveText(self):
            with open("3dcart_info_Goes_Here.txt", 'w') as file: #Open the file
                    my_text = self.EmailTextBox.toPlainText() #Set the text to write
                    file.write(my_text) #Write that text to a file
                    file.close() #Close the file.
                    
    def parseEmail(self):
            try:
                    with open("3dcart_info_Goes_Here.txt", 'r') as file:
                            for i, lines in enumerate(file):
                                    
                                    #transaction center id credentials
                                    transid = re.search(r'TranCenter', lines)
                                    if transid:
                                            global Gtransid
                                            Gtransid = lines[15:]

                                    #email
                                    emailTo = re.search(r'Email address for merchant is', lines)
                                    if emailTo:
                                             global Gemail
                                             Gemail = lines[31:]
                                             
                                    username = re.search(r'User Name', lines)
                                    if username:
                                            global Gusername
                                            Gusername = lines[11:]
                                            
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
                                    if ((hostftp) and i in range(48,68)):
                                            global Ghostftp
                                            Ghostftp = lines[:-2]
                                            
                                    loginftp = re.search(r'\|', lines)
                                    if loginftp:
                                            global Gloginftp
                                            Gloginftp = lines[7:-2]
                                            
                                    passftp = re.search(r'Password:', lines)
                                    if passftp and i in range(50,70):
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
                
    def createEmail(self):
        outlook = win32.Dispatch('outlook.application') #Open Outlook
        mail = outlook.CreateItem(0) #Create an email.
        mail.To = Gemail #Send to Merchant's email that we have parsed.
        mail.Subject = "" #Subject of email.
        text = ""
        mail.Body = text #Set body to the text above.
        if mail.Display(False): #Open the email that we want to compose to outlook.
           mail.Display(True)

    def sendftp(self):
        #This method is for writing the script that will be read by winscp.
        #At the end we will invoke the program with cmd and tell winscp to read
        #the script that we create in this method.
        
        text2write = "open \"ftps://" + Gloginftp + ':' + Gpassftp +'@'+ Ghostftp + '\"\n'
        text2write += 'cd /keys\n' 
        text2write += 'put "c:path\to\file\gw_ids.txt"\n' #change to valid path
        text2write += 'put "c:path\to\file\gw_ids1.txt"\n' #change to valid path
        text2write += 'cd ../web/assets\n' #change to valid path
        text2write += 'put "c:\path\to\3dCart Branding\\brandv7"\n' #change to valid path
        text2write += "exit"
        
        with open("scpScript.txt", 'w') as scpfile:
            scpfile.write(text2write)
            scpfile.close()
                
        dirScpFile = os.path.realpath(scpfile.name)
        result = '"' + dirScpFile + '"'
        print("Made the SCP Script")
        command = "winscp.com /script=" + result
        os.system("start cmd /k " + command)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())
