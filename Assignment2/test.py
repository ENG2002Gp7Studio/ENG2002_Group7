import os
import datetime
import user_management_system.user_management_sys as ums
import phonebook_package.phonebook as pb
#import phonebook_package.phonebook as pb

# def ums_encryption(ip):

#         op = ""
#         for i in range(0, len(ip)):
#             op += chr(ord(ip[i]) + 129)

#         return op

# def ums(ip):

#         op = ""
#         for i in range(0, len(ip)):
#             op += chr(ord(ip[i]) - 129)

#         return op

# user = [ums.UserInfo(False, "QuintinUmi"), ums.UserInfo(False, "Cocoa"), ums.UserInfo("1913176928", "Cocoa")]
# uPwd = ["wwdfj.d", "Cocoa", "I love cocoa"]
# userA = ums.UserManageSys("H:\\test")
# if(userA.sys_status == -3):
#     userA.database_built_up("H:\\test", user, uPwd)

# userA.user_log_in("QuintinUmi", "wwdfj.d")
# print(userA.sys_status)

# userA.user_sign_up("QuintinUmi", "wwdfj.d")
# print(userA.sys_status)

# userA.user_sign_up("123", "wwdfj.d")
# print(userA.sys_status)

# userA.user_log_in("QuintinUmi", "wwdfj.d")
# print(userA.sys_status)

# userA.user_sign_up("123", "wwdfj.d")
# print(userA.sys_status)

# userA.user_log_out()
# print(userA.sys_status)

# userB = ums.UserManageSys("H:\\test", user[2], "I love cocoa")
# print(userB.userInfo.userID)

# ums.show_user_database("H:\\test")

# rcd = [pb.phoneRec()]
# pb1 = pb.phoneBk("H:\\test1\\abs\\rec.pb", rcd)

# print(datetime.datetime.now())

# a = [0, 1, 2, 3]
# b = "0123456"
# print(b[0: 1])
# if(False == 5):
#     print("yes")

# a = open("H:\\test.txt", "w")
# a.write("123456789\nabcdefghi\n987654321\n")
# a.close()
# a = open("H:\\test.txt", "r")
# b = a.readlines()
# a.close()
# print(b)
# a = open("H:\\test.txt", "r+")
# a.readline()
# w = a.readline()
# l = len(w)
# a.seek(a.tell() - l - 1)
# a.write(' ' * l)
# a.seek(a.tell() - l)
# a.write("89")
# a.close()

# class ABC:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

# a = int("abc")

# jicheng = ABC(1, 2, 3)

# print(ABC(1, 2, 3).a)

# a = [ABC(1, 2, 3), ABC(4, 5, 6), ABC(7, 8, 9)]
# print(a[0].a)


# class int():
#     def __init__(self, number):
        

#         temp = str(number)
#         temp = temp.split('.')
#         self.a = temp[0]
#         self.b = temp[1]

# math = [int(5.3), int(4.2), int(6.8)]

# print(math[0].a)
# print(math[1].b)
# def func():
#     try:
#         f = open("H:\\sss.txt", "r")

#     except OSError:
#         print("Error")
#         return -1

#     print("good")
#     return 0

# test = [pb.phoneRec("123456",1, '12315', '1231654,', '156156', '131654646'), pb.phoneRec("123456",1, '12315', '1231654,', '156156', '131654646')]
# print(test[0].email)

# t = pb.phoneBk("H:kkk.sss")
# print(t.ph_status)

# t = ums.UserManageSys("H:sss")
# print(t.sys_status)
print("012131321313131031201313101030123130".isnumeric())
a = "sss-sss-sss 123:2465:534"
a = 'Peter'.upper()
print('12'>'4')



