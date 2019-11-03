#!/bin/bash

# ------- FORMATTING --------------------------------------
OK="[\033[32mOK\e[0m]"
CHECKDIR="[\033[32mCHECK\e[0m]"
WAR="[\033[31mWARNING!\e[0m]"
INFO="[\033[34mINFO\e[0m]"
INFOW="[\033[31mINFO\e[0m]"
MODIFIED="[\033[31mMODIFIED\e[0m]"
MODIFIED_PATH="[\033[93mMODIFIED PATH\e[0m]"
LAST_MODIFIED_DATE="[\033[93mLAST MODIFIED DATE\e[0m]"
ORGINAL="[\033[32mORGINAL\e[0m]"
# -----------------------------------------------------
TODAY=$(date "+%m-%d-%y")
YESTERDAY=$(date -d "1 day ago" '+%m-%d-%y')

HEADER() {
echo ""
echo -e "----------- $1 $2  ------------" 
echo ""
}

DEBUG() {
echo -e "$1" "$2"
}

CHECKSUM(){
    echo $(du -sh "/$1" 2>/dev/null |awk '{print $1}' | sha1sum | awk '{print $1}') "/$1" >> log/$TODAY
}


CHECK_DIFF(){

    if [ -e "log/$TODAY" ];then
            
        DEBUG $CHECKDIR "CHECK LOG FILE: $DATE"
        DEBUG $CHECKDIR "COMPARE LOGS: from $TODAY to $YESTERDAY"
                
        DIFF=$(diff -q "log/$TODAY" "log/$YESTERDAY")
                    
        # MORE DETAIL ABOUT SUSPICIOUS FILE
        
        if [ "$DIFF" != "" ];then
            DEBUG "$WAR" "THE FILE HAS BEEN MODIFIED"
            differ=$(diff -y "log/$TODAY" "log/$YESTERDAY" | awk '{print $5}') # GET PATH
            
            for i in $differ;do
                DEBUG "\t$MODIFIED_PATH" $i
            done
            
        # ---------------------------------------------------------
        else
        
            DEBUG "$OK" "FILE OK"
                
        fi
    else
    
        DEBUG $INFO "CREATE LOG FILE FOR: $DIR"
        CHECKSUM $DIR
    fi

}

CHECK_DIR(){
    
    DIRECTORY="tmp home/$USER"
    
    # IF LOG FILE BEING, THEN CHECK LOGS
    if [ -e "log/$TODAY" ];then
        CHECK_DIFF
    else
        for DIR in $DIRECTORY;do
            HEADER $INFO "CHECK /$DIR DIR"
            
            # IF CHECKING DIR EXIST THEN
            if [ -d "/$DIR" ];then
                CHECKSUM $DIR
                
            # IF DOESN'T EXITS SHOW
            else
                DEBUG "$INFOW" "DIR/FILE DOESN'T EXIST"
            fi
            
        done
    fi
}

CHECK_DIR



