#!/bin/bash

if [ -f /etc/zce.rc ];then
    . /etc/zce.rc
else
    echo "/etc/zce.rc doesn't exist!"
    exit 1;
fi
if [ -f $ZCE_PREFIX/bin/shell_functions.rc ];then
    . $ZCE_PREFIX/bin/shell_functions.rc
else
    echo "$ZCE_PREFIX/bin/shell_functions.rc doesn't exist!"
    exit 1;
fi
if [ ! -f $ZCE_PREFIX/gui/application/data/zend-server-user.ini ];then
    echo "missing $ZCE_PREFIX/gui/application/data/zend-server-user.ini, your installation must be corrupted, try to reinstall"
    exit 1;
fi
check_root_privileges
get_passwd()
{
    echo "Please insert a password to access the $PRODUCT_NAME UI: "
    stty -echo
    read PASS
    if [ ${#PASS} -lt 4 ];then 
        echo "Password should be 4 characters minimum."
        return 1
    fi
    echo "Verify password: "
    read PASS_VER
    stty echo
    if [ "$PASS" != "$PASS_VER" ];then
        echo "Passwords don't match. Please try again."
        return 1
    fi
    PASS_OK=1
    return 0
}
if [ -n "$ZEND_SERVER_PASSWD" ];then
    PASS=$ZEND_SERVER_PASSWD
    PASS_OK=1
else
    while [ -z $PASS_OK ];do
        get_passwd
    done
fi
MD5=`echo -n $PASS|$MD5BIN|cut -d ' ' -f1`
perl -pe "s/password\s*=\s*.*$/password=$MD5/" -i $ZCE_PREFIX/gui/application/data/zend-server-user.ini 
if [ $? -eq 0 ];then
    echo "GUI password updated successfully."
else
    echo "Failed to update GUI password!"
fi
