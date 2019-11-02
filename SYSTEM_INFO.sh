#!/bin/bash

OK="[\033[32mOK\e[0m]"
WAIT="[\033[32m*\e[0m]"
CHECKDIR="[\033[32mCHECK\e[0m]"
WAR="[\033[31m!\e[0m]"
INFO="[\033[34mINFO\e[0m]"
INFOW="[\033[31mINFO\e[0m]"

HEADER() {
echo ""
echo -e "----------- $1 $2  ------------" 
echo ""
}

HEADER $INFO "CHECK SYSTEM CONFIGURATION"
echo -e "$INFO Host_name        :" $(hostname)
echo -e "$INFO Os_version       :" $(uname -v)
echo -e "$INFO Architecture     :" $(uname -m)
echo -e "$INFO Kernel           :" $(uname -r) | sed 's/-.*//'
echo -e "$INFO OS_FULLNAME      :" $(grep "^VERSION_ID=" /etc/os-release | awk -F= '{print $2}' |tr -d '"')
echo -e "$INFO OS               :" $(grep "^VERSION=" /etc/os-release | awk -F= '{print $2}' |tr -d '"')
echo -e "$INFO Default Shell    :" $SHELL
echo -e "$INFO Bash_version     :" $BASH_VERSION
