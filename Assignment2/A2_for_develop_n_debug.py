#####################################################################################
#   This is for programming develop and debug only, but not for the final product   
#                                                                                   
#####################################################################################

import phonebook_package.phonebook as pb
import user_management_system.user_management_sys as ums



userInfo, userAccess = ums.UserManageSys.sys_init()
if(userAccess):
    pb.phoneBk.sys_init(userInfo)



