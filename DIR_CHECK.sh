#!/bin/bash

OK="[\033[32mOK\e[0m]"
CHECKDIR="[\033[32mCHECK\e[0m]"
WAR="[\033[31mWARNING!\e[0m]"
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
echo $(du -sh $1 2>/dev/null |awk '{print $1}' | sha1sum | awk '{print $1}') $1 > $(date +"%m-%d-%y")
}

CHECK_DIR(){
    DIR="tmp"
    
    local TODAY=$(date "+%m-%d-%y")
    local YESTERDAY=$(date -d "1 day ago" '+%m-%d-%y')
    
    
    if [ -d "/$DIR" ];then
    
        HEADER $INFO "CHECK /$DIR DIR" 	
    
        if [ -e "log/$TODAY" ];then
    
            DEBUG $CHECKDIR "CHECK LOG FILE: $DATE"
            # echo $(du -sh /tmp 2>/dev/null |awk '{print $1}' | sha1sum | awk '{print $1}') $1 > ./log/"$(date +'%m-%d-%y')" 

            if [ -e "log/$YESTERDAY" ];then
                DEBUG $CHECKDIR "COMPARE LOGS: from $TODAY to $YESTERDAY"
                DIFF=$(diff -q log/$TODAY log/$YESTERDAY)
            
                if [ "$DIFF" != "" ];then
                
                    DEBUG "$WAR" "THE FILE HAS BEEN MODIFIED"
                    DEBUG "$INFOW" "LAST MODIFIED"
                else
                    DEBUG "$OK" "FILE OK"
                
                fi
            else
                DEBUG "$INFOW" "NOTHING TO COMPARE"
            fi
        
        else
    
            DEBUG $INFO "CREATE LOG FILE FOR: /tmp"
            echo $(du -sh /tmp 2>/dev/null |awk '{print $1}' | sha1sum | awk '{print $1}') $1 > log/"$TODAY"       
        
        fi
    else
        
        DEBUG "$INFOW" "FILE DOESN'T EXIST"
    fi
}
CHECK_DIR
