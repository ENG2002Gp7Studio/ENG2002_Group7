
import os
import sys
import datetime

class UserInfo:
    def __init__(self, userID, userName):
        self.userID = userID
        self.userName = userName


class UserManageSys:

    def __init__(self, userInfo = -1, userPwd = -1):  
                                                #User system init
        self.userInfo = userInfo
        self.userDataBase = []
        self.uDBRootPath = -1
        self.userAccess = False
        self.sys_init(userPwd)

    
    def sys_init(self, userPwd = -1):
        
        if(self.userInfo == -1):
            return self.menu()
        else:
            return self.user_check(self.userInfo.userName, userPwd)



    def menu(self):

        while(self.uDBRootPath == -1):
            self.file_location_detect()

        while(True):
            print("**********************************************************************")
            print("*   Welcome to use ENG2002 Group7 Smart User Management System!      *")
            print("*   Please Choose the option below:                                  *")
            print("*                                                                    *")
            print("*   1. Login-in                                                      *")
            print("*   2. Sign-in                                                       *")
            print("*   3. Exit                                                          *")
            print("*                                                                    *")
            print("**********************************************************************")

            ip = str(input("Input the number and Enter to continue: "))
            if('1' <= ip <= '3'):
                break

        if(ip == "1"):
            
            while(True):
                os.system("cls")
                ipUserID = input("Please input user NAME or ID: ")  
                userID, userName, userStatus = self.user_check(ipUserID)    # -2: User not exist; -1: Password Error; 0: Access; 1: User exist

                if(userStatus == -2):    
                    while(True):
                        os.system("cls")
                        print("**********************************************************************")
                        print("Dear {}, ".format(ipUserID))
                        print("You haven't an account yet. Do you want to")
                        print("1. Create an Account With User Name \"{}\"".format(ipUserID))
                        print("2. Change User")
                        print("3. Exit")
                        print("**********************************************************************")
                        ip = str(input("Input the number and Enter to continue:"))
                        if('1' <= ip <= '3'):
                            break

                    if(ip == '1'):
                        while(True):
                            os.system("cls")
                            print("UserName: {}".format(ipUserID))
                            print("Please input your Password:\n")
                            st_pwd = input()
                            os.system("cls")
                            print("Please input your Password:\n\n" + len(st_pwd) * '*')
                            print("\nPlease input your Password again:\n")
                            nd_pwd = input()
                            print("\n")

                            if(st_pwd != nd_pwd):
                                print("Two passwords are different, please input again!")
                                os.system("PAUSE")
                            else:
                                break
                        
                        self.user_database_write(ipUserID, nd_pwd)
                        userID, userName, userStatus = self.user_check(ipUserID)
                        pwdLen = len(nd_pwd)
                        nd_pwd = 0

                        self.sign_in_show(pwdLen, userID, userName)
                        return userID, userName, userStatus


                    if(ip == '2'):
                        continue

                    if(ip == '3'):
                        self.exit_show()
                        exit(0)

                if(userStatus == 1):

                    for i in range(5, -1, -1):
                        
                        os.system("cls")
                        print("UserName: {}".format(ipUserID))
                        ipUserPwd = input("Please input password: ")
                        userID, userName, userStatus = self.user_check(ipUserID, ipUserPwd)
                        pwdLen = len(ipUserPwd)
                        ipUserPwd = 0
                        if(userStatus == 0):
                            self.userInfo = UserInfo(userID, userName)
                            self.userAccess = True
                            self.log_in_show(pwdLen, userID, userName)
                            return userID, userName, 0
                        else:
                            print("Password Error! You have {} time(s) left to try.\n".format(i))
                            os.system("PAUSE")

                    os.system("cls")
                    print("Input wrong password too many times! Please try again later!")
                    os.system("PAUSE")
                    exit(0)

        if(ip == "2"):

            while(True):

                os.system("cls")
                ipUserName = input("Please input your user NAME: ")  
                userID, userName, userStatus = self.user_check(ipUserName)    

                if(userStatus == 1):
                    print("\nThis user NAME has been exist. Please try another NAME.\n")
                    os.system("PAUSE")
                    continue
                else:
                    break

            while(True):
                os.system("cls")
                print("UserName: {}".format(ipUserName))
                print("Please input your Password:\n")
                st_pwd = input()
                os.system("cls")
                print("Please input your Password:\n\n" + len(st_pwd) * '*')
                print("\nPlease input your Password again:\n")
                nd_pwd = input()
                print("\n")

                if(st_pwd != nd_pwd):
                    print("Two passwords are different, please input again!")
                    os.system("PAUSE")
                else:
                    break
                    
            self.user_database_write(ipUserName, nd_pwd)
            userID, userName, userStatus = self.user_check(ipUserName)
            pwdLen = len(nd_pwd)
            nd_pwd = 0

            self.userInfo = UserInfo(userID, userName)
            self.userAccess = True
            self.sign_in_show(pwdLen, userID, userName)

            return userID, userName, userStatus

        if(ip == "3"):
            os.system("cls")
            self.exit_show()
            exit(0)


    def log_in_show(self, pwdLen, userID, userName):
        os.system("cls")
        print("UserName: {}".format(userName))
        print("Please input password: " + pwdLen * '*')
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("                     Login in success!                         ")
        print("---------------------------------------------------------------")
        print("Login in Date: {}".format(datetime.datetime.now()))
        print("User ID: \t{}".format(userID))
        print("User Name: \t{}".format(userName))
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        os.system("PAUSE")
        os.system("CLS")

    def sign_in_show(self, pwdLen, userID, userName):
        os.system("cls")
        print("UserName: {}".format(userName))
        print("Please input password: " + pwdLen * '*')
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("                         Sign in success!                        ")
        print("-----------------------------------------------------------------")
        print("Sign in Date: {}".format(datetime.datetime.fromtimestamp(userID[len(userID) - 10 - 1 : len(userID) - 1])))
        print("User ID: \t{}".format(userID))
        print("User Name: \t{}".format(userName))
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        os.system("PAUSE")
        os.system("CLS")

    def exit_show(self):
        os.system("cls")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(" Thank you ")
        print("             for using ")
        print("                         ENG2002 Group7")
        print("                                         Smart User Management System! ")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        os.system("PAUSE")

    # def user_sign_in():
    #     pass

    def user_del():
        pass




    def user_check(self, userID, userPwd = -1):
        
        userAll = self.user_database_read()
        if(userPwd == -1):

            if(userAll == -2):
                return -2, -2, -2
            
            for user in userAll:
                if(self.ums_encryption(userID) in user):
                    return self.ums_decryption(user[0]), self.ums_decryption(user[1]), 1
                else:
                    return -2, -2, -2

        else:

            if(not(self.ums_encryption(userID) in userAll[0] or self.ums_encryption(userID) in userAll[1])):
                return -2, -2, -2
            
            for i in range(0, len(userAll)):

                if(userAll[i][0] == self.ums_encryption(userID) or userAll[i][1] == self.ums_encryption(userID)):
                    if(userAll[i][2] == self.ums_encryption(userPwd)):
                        return self.ums_decryption(userAll[i][0]), self.ums_decryption(userAll[i][1]), 0
                    else:
                        return self.ums_decryption(userAll[i][0]), self.ums_decryption(userAll[i][1]), -1



        


    def user_database_read(self):
                                                                         # ID + Name + Pwd
        userFile = open(self.uDBRootPath + ":\\UserManagementSystem\\userDataBase.ums", 'r', encoding='utf-8')

        if(len(userFile.readline()) == 0):
            userFile.close()
            return -2

        userFile.seek(0)

        userAll = []
        while(True):

            rd_temp = userFile.readline()

            if(rd_temp == ""):
                break

            user_temp = rd_temp.split('*')
            user_temp[2] = user_temp[2][0:len(user_temp[2]) - 1]

            userAll.append(user_temp)
        
        userFile.close()

        return userAll


    def user_database_write(self, userName, userPwd, ins = False):

        if(not ins):

            userID = self.user_id_create(userName)

            userFile = open(self.uDBRootPath + ":\\UserManagementSystem\\userDataBase.ums", 'a', encoding='utf-8')
            w_temp = self.ums_encryption(userID) + '*' + self.ums_encryption(userName) + '*' + self.ums_encryption(userPwd)
            userFile.write(w_temp + '\n')
            userFile.close()    

            return 0

        else:

            userFile = open(self.uDBRootPath + ":\\UserManagementSystem\\userDataBase.ums", 'w', encoding='utf-8')

            while(True):
                user_temp = userFile.readline()
                if(user_temp == ""):
                    userFile.close()
                    return -2

                user_temp = user_temp.split('*')
                if(user_temp[1] == self.ums_encryption(userName)):
                    userFile.seek(userFile.tell() - len(user_temp))
                    userFile.write(user_temp[0] + '*' + self.ums_encryption(userName) + '*' + self.ums_encryption(userPwd) + '\n')
                    break
            
            userFile.close()
            return 0

            


   

    def file_location_detect(self):

        locationAccess = False
        fileDisk = 'Z'
        while(fileDisk >= 'A'):
            if(os.path.isfile(fileDisk + ":\\UserManagementSystem\\sysInit.check") and 
                os.path.isfile(fileDisk + ":\\UserManagementSystem\\userDataBase.ums")):
                locationAccess = True
                break
            if(os.path.isfile(fileDisk + ":\\UserManagementSystem\\userDataBase.ums")):
                f_temp = open(fileDisk + ":\\UserManagementSystem\\sysInit.check", "w")
                f_temp.close()
                locationAccess = True
                break
            if(os.path.isfile(fileDisk + ":\\UserManagementSystem\\sysInit.check")):
                f_temp = open(fileDisk + ":\\UserManagementSystem\\userDataBase.ums", "w")
                f_temp.close()
                self.uDBRootPath = fileDisk
                return 0

            fileDisk = chr(ord(fileDisk) - 1)
        
        if(locationAccess):
            self.uDBRootPath = fileDisk
        else:
            fileDisk = '0'
            print("Is the first time to use UserManagementSystem(UMS)?")
            print("Please input an accessible Disk(A~Z) for storage the UMS Data")
            print("(NOTE: If the Disk cannot access, the software may crash!)")
            while(not('A' <= fileDisk <= 'Z' or 'a' <= fileDisk <= 'z')):
                fileDisk = input("Disk(Enter '0' to EXIT): ")
                if(fileDisk == '0'):
                    sys.exit(0)
                if(not('A' <= fileDisk <= 'Z' or 'a' <= fileDisk <= 'z')):
                    print("Please input an accessible Disk(A~Z) for storage the UMS Data")

            if(not os.path.exists(fileDisk + ":\\UserManagementSystem")):
                os.mkdir(fileDisk + ":\\UserManagementSystem")
            f_temp = open(fileDisk + ":\\UserManagementSystem\\sysInit.check", "w")
            f_temp.close()
            f_temp = open(fileDisk + ":\\UserManagementSystem\\userDataBase.ums", 'w')
            f_temp.close()

            if(os.path.isfile(fileDisk + ":\\UserManagementSystem\\sysInit.check")):
                self.uDBRootPath = fileDisk
            else:
                print("System Error: 001\nFile cannot be created!")
                self.uDBRootPath = -1


    def user_id_create(self, userName):
        userID = ""
        for i in range(len(userName)):
            userID += str(ord(userName[i])%10)
        userID += str(int(datetime.datetime.timestamp(datetime.datetime.now())))
        return userID
        
    def ums_encryption(self, ip):

        op = ""
        for i in range(0, len(ip)):
            op += chr(ord(ip[i]) + 35409)

        return op

    def ums_decryption(self, ip):

        op = ""
        for i in range(0, len(ip)):
            op += chr(ord(ip[i]) - 35409)

        return op
