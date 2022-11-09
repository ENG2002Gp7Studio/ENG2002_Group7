#####################################################################################
#   This is for programming develop and debug only, but not for the final product   
#                                                                                   
#####################################################################################

import os
import sys
import datetime
import phonebook_package.phonebook as pb
import user_management_system.user_management_sys as ums



def main():
    user = ums.UserManageSys()
    # ums.show_user_database(user.uDBRootPath)
    # input()
            
    if(user.userAccess):
        
        while(True):

            timeList = pb.phoneBk.time_split_str(pb.phoneBk, datetime.datetime.now())

            if(0 <= int(timeList[3]) <= 5):
                greeting = "Good morning"
            if(5 < int(timeList[3]) <= 12):
                greeting = "Good morning"
            if(12 < int(timeList[3]) <= 17):
                greeting = "Good afternoon"
            if(17 < int(timeList[3]) <= 23):
                greeting = "Good evening"

            while(True):
                os.system("cls")
                print("**********************************************************************")
                print("*   {}, dear {}  ".format(greeting, user.userInfo.userName))
                print("*                                                                    *")
                print("*   Please Choose the option below:                                  *")
                print("*                                                                    *")
                print("*   1. Enter Phone Book System                                       *")
                print("*   2. Change Password                                               *")
                print("*   3. Log out                                                       *")
                print("*   4. Exit                                                          *")
                print("*                                                                    *")
                print("**********************************************************************")

                ip = str(input("\nInput the number and Enter to continue: "))
                if('1' <= ip <= '4'):
                    break
            
            if(ip == '1'):
                pbFilePath = user.uDBRootPath[0] + ':\\PhoneBookSystem\\' + str(user.userInfo.userID) + ".pb"
                uPhoneRec = pb.phoneBk(pbFilePath)
                uPhoneRec.built_in_menu()


            if(ip == '2'):
                os.system("cls")
                print("Please input your original password: \n")
                oriPwd = input()
                t1, t2, pwdCheck, t4 = user.user_check(user.userInfo.userID, oriPwd)
                if(pwdCheck == -1):
                    print("\nWrong Password!\n")
                    os.system("PAUSE")
                    continue
                if(pwdCheck == 0):
                    while(True):
                        os.system("cls")
                        print("UserName: {}".format(user.userInfo.userName))
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
                    user.user_database_write(user.userInfo.userName, nd_pwd, True, user.userInfo.userID)
                    os.system("cls")
                    print("Please input your Password:\n\n" + len(st_pwd) * '*')
                    print("\nPlease input your Password again:\n\n" + len(st_pwd) * '*')
                    print("\nChange password successfully!\n")
                    os.system("PAUSE")

                else:
                    sys.exit("Unknown Error!")


            if(ip == '3'):
                user.user_log_out()
                os.system("cls")
                print(">>>>>>>>>>>>>>>>>>>>")
                print("  Log out success!  ")
                print(">>>>>>>>>>>>>>>>>>>>\n")
                os.system("PAUSE")
                user.built_in_menu()
                continue
            if(ip == '4'):
                user.exit_show()
                exit(0)

if __name__ == "__main__":
    main()
