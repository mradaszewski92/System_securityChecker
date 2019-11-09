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
FILE_DETAIL="[\033[36mFILE DETAIL\e[0m]"
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
    echo $(du -shb "/$1" 2>/dev/null |awk '{print $1}' | sha1sum | awk '{print $1}') "/$1" >> log/$TODAY
}
get_file_status(){

    mod_file=$1
    
    file_name=$(stat -c %n "$mod_file") #-file name
    file_type=$(stat -c %F "$mod_file") #-file type
    id_of_owner=$(stat -c %u "$mod_file") #-user ID of owner 
    group_of_owner=$(stat -c %G "$mod_file") #-group name of owner
    user_of_owner=$(stat -c %U "$mod_file") #-user name of owner 
    access_right=$(stat -c %A "$mod_file") #-access rights in human readable form
    mount_point=$(stat -c %m "$mod_file") #-mount point
    hard_links=$(stat -c %h "$mod_file") #-number of hard links
    total_size=$(stat -c %s "$mod_file") #-total size, in bytes 
    
    modify_date=$(stat "$mod_file" | grep 'Modify' |awk '{print $2}')
    modify_time=$(stat "$mod_file" | grep 'Modify' |awk '{print $3}')
    
    id_of_owner_dsp="\e[91m$id_of_owner\e[0m"
    group_of_owner_dsp="\e[91m$group_of_owner\e[0m"
    access_right_dsp="\e[91m$access_right\e[0m"
    file_type_dsp="\e[32m$file_type\e[0m"
    mount_point_dsp="\e[32m$mount_point\e[0m"
    hard_links_dsp="\e[32m$hard_links\e[0m"
    
    # \e[91mLight red

    # DEBUG "\t\t$LAST_MODIFIED_DATE" "DATE:$modify_date TIME:$modify_time"
    DEBUG "\t\t$FILE_DETAIL" "Owner ID:$id_of_owner_dsp GUID:$group_of_owner_dsp Rights:$access_right_dsp"
    DEBUG "\t\t$FILE_DETAIL" "Type:$file_type_dsp   Mount_point:$mount_point_dsp hard_links:$hard_links_dsp"

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
                get_file_status "$i"
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
    
    DIRECTORY="dev proc run sys etc media boot home mnt opt bin root srv tmp usr lib lib32 lib64 libx32 sbin var"
    
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
