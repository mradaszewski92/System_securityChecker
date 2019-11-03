#!/bin/bash

OK="[\033[32mOK\e[0m]"
CHECKDIR="[\033[32mCHECK\e[0m]"
WAR="[\033[31mWARNING!\e[0m]"
INFO="[\033[34mINFO\e[0m]"
INFOW="[\033[31mINFO\e[0m]"
MODIFIED="[\033[31mMODIFIED\e[0m]"
LAST_MODIFIED_DATE="[\033[93mLAST MODIFIED DATE\e[0m]"
ORGINAL="[\033[32mORGINAL\e[0m]"

TODAY=$(date "+%m-%d-%y")
YESTERDAY=$(date -d "1 day ago" '+%m-%d-%y')

HEADER() {
echo ""
echo -e "----------- $1 $2  ------------" 
echo ""
}

DEBUG() {
echo -e $1 $2
}

CHECKSUM(){
echo $(du -sh $1 2>/dev/null |awk '{print $1}' | sha1sum | awk '{print $1}') "/$1" > log/$TODAY
}

CHECK_DIR(){
    
    DIRECTORY="tmp "
    
    for DIR in $DIRECTORY;do
    
        if [ -d "/$DIR" ];then
    
            HEADER $INFO "CHECK /$DIR DIR" 	
    
            if [ -e "log/$TODAY" ];then
    
                DEBUG $CHECKDIR "CHECK LOG FILE: $DATE"

                if [ -e "log/$YESTERDAY" ];then
                
                    DEBUG $CHECKDIR "COMPARE LOGS: from $TODAY to $YESTERDAY"
                    DIFF=$(diff -q "log/$TODAY" "log/$YESTERDAY")
                    
                    
                 
                    if [ "$DIFF" != "" ];then
                        
                        mod_file=$(cat "log/$TODAY" | awk '{print $2}')
                        log_today_sha1=$(cat "log/$TODAY" | awk '{print $1}')
                        log_yesterday_sha1=$(cat "log/$YESTERDAY" | awk '{print $1}')

                        modify_date=$(stat $mod_file | grep 'Modify' |awk '{print $2}')
                        modify_time=$(stat $mod_file | grep 'Modify' |awk '{print $3}')
                        file_name=$(stat $mod_file | grep 'File' |awk '{print $2}')
                        
                        DEBUG "$WAR" "THE FILE HAS BEEN MODIFIED"
                        DEBUG "\t$MODIFIED" "SHA1: $log_today_sha1"
                        DEBUG "\t$ORGINAL" "SHA1: $log_yesterday_sha1"
                        DEBUG "\t$LAST_MODIFIED_DATE" "DATE:$modify_date TIME:$modify_time" 
                        
                        # ---------------------------------------------------------
                        
                        
                    else
                
                        DEBUG "$OK" "FILE OK"
                
                    fi
                else
                    
                    DEBUG "$INFOW" "NOTHING TO COMPARE"
                fi
        
            else
    
                DEBUG $INFO "CREATE LOG FILE FOR: /tmp"
                CHECKSUM $DIR
        
            fi
        else
        
            DEBUG "$INFOW" "FILE DOESN'T EXIST"
    fi
    
    done
}

CHECK_DIR

# future functionality
# DIR="tmp home/$USER"
# 
# for i in $DIR;do
#     
#     echo " ----------------$i-------------------------------"
# 
#     DATA=$(ls -l "/$i" |awk '{print $9}')
#     
#     'File\|Access\Modify\|Change'
#     for j in $DATA;do
#          stat /$i/$j | grep 'File\|Access\|Modify\|Change'
#         
#     done
# done



