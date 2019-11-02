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

DEBUG() {
echo -e $1 $2

}

CHECKSUM(){
echo $(du -sh $1 2>/dev/null |awk '{print $1}' | sha1sum | awk '{print $1}') $1 >> log          
}


HEADER $INFO "CHECK TMP DIR" 	
if [ -e "/$1" ];then
DEBUG $INFO  "$1 ALREADY EXIST"
DEBUG $CHECKDIR "CHECK /$1 DIR"
if [ -e "log" ];then
	DEBUG $WAIT "VERIFIES CHECKSUM"
	DIFF=$(diff -q log log1)
	if [ "$DIFF" != "" ];then
		DEBUG $INFOW "INVALID CHECKSUM"
	else
		DEBUG $OK "CHECKSUM VALID"
	fi

else
	DEBUG $INFO "CREATE CHECKSUM"
	CHECKSUM "/tmp"
	# echo $(du -sh /tmp 2>/dev/null |awk '{print $1}' | sha1sum | awk '{print $1}') $1 >> log 
fi
else
DEBUG $WAIT "DIR DOESN'T EXIST"
fi
