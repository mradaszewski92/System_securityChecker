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


DOT="."
dir="."
HEADER $OK "CHECK $1 DIRECTORY"

if [ -n $PATH ];then

	PATH1=${PATH}
	envPath=$(echo "${PATH1}" | tr ':' ' ')	
	DIRECTORY="/usr ."	
	
	for dir in $DIRECTORY;do
		# data = $(ls -l -d .[!.]?* | awk '{print $9}')
		DEBUG $CHECKDIR "CHECKING $dir"
		HIDDEN_FILE=$(find $dir -maxdepth 1 -name ".*" -print)
		
		if [ "$HIDDEN_FILE" != "" ] && [ "$HIDDEN_FILE" != "." ];then

		DEBUG $INFOW "FOUND SUSPICIUS HIDDEN FILE/S"

			for file in $HIDDEN_FILE;do
				DEBUG "\t$WAR" "SUSPICIOUS FILE: $file"
			done
		else
			DEBUG "$INFO" "NOT FOUND HIDDEN FILES/DIRECTORIES. PATH OK"
		fi
	done
fi

