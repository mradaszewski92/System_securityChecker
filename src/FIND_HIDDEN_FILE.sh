#!/bin/bash

OK="[\033[32mOK\e[0m]"
WAIT="[\033[32m*\e[0m]"
CHECKDIR="[\033[32mCHECK\e[0m]"
WAR="[\033[31m!\e[0m]"
INFO="[\033[34mINFO\e[0m]"
INFOW="[\033[31mINFO\e[0m]"
DNG_SUID="[\033[31mDENGEROUS PERMISION\e[0m]"

function HEADER {
echo ""
echo -e "----------- $1 $2  ------------" 
echo ""
}
DEBUG() {
echo -e $1 $2
}


DOT="."
dir="."

# HEADER $OK "CHECK $1 DIRECTORY"
# 
# if [ -n $PATH ];then
# 
# 	PATH1=${PATH}
# 	envPath=$(echo "${PATH1}" | tr ':' ' ')	
# 	DIRECTORY="/usr ."	
# 	
# 	for dir in $DIRECTORY;do
# 		data = $(ls -l -d .[!.]?* | awk '{print $9}')
# 		DEBUG $CHECKDIR "CHECKING $dir"
# 		HIDDEN_FILE=$(find $dir -maxdepth 1 -name ".*" -print)
# 		
# 		if [ "$HIDDEN_FILE" != "" ] && [ "$HIDDEN_FILE" != "." ];then
# 
# 		DEBUG $INFOW "FOUND SUSPICIUS HIDDEN FILE/S"
# 
# 			for file in $HIDDEN_FILE;do
# 				DEBUG "\t$WAR" "SUSPICIOUS FILE: $file"
# 			done
# 		else
# 			DEBUG "$INFO" "NOT FOUND HIDDEN FILES/DIRECTORIES. PATH OK"
# 		fi
# 	done
# fi

FIND_SUID_GUID(){

    HEADER "$INFO" "LOKING FOR SUID/GUID FILE"

    SUID_GUID_FILE=$(find / \( -perm -4000 -o -perm -2000 \) -type f -exec ls {} \; 2>/dev/null)
    
    for i in $SUID_GUID_FILE;do
        DEBUG "$DNG_SUID" "$i"
    done

}

get_file_status(){

    mod_file=$1
    
    file_name=$(stat -c %n "$mod_file" 2>/dev/null) #-file name
    file_type=$(stat -c %F "$mod_file" 2>/dev/null) #-file type
    id_of_owner=$(stat -c %u "$mod_file" 2>/dev/null) #-user ID of owner 
    group_of_owner=$(stat -c %G "$mod_file" 2>/dev/null) #-group name of owner
    user_of_owner=$(stat -c %U "$mod_file" 2>/dev/null) #-user name of owner 
    access_right=$(stat -c %A "$mod_file" 2>/dev/null) #-access rights in human readable form
    mount_point=$(stat -c %m "$mod_file" 2>/dev/null) #-mount point
    hard_links=$(stat -c %h "$mod_file" 2>/dev/null) #-number of hard links
    total_size=$(stat -c %s "$mod_file" 2>/dev/null) #-total size, in bytes 
    
    modify_date=$(stat "$mod_file" 2>/dev/null| grep 'Modify' |awk '{print $2}')
    modify_time=$(stat "$mod_file" 2>/dev/null| grep 'Modify' |awk '{print $3}')
    
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



HIDEN_FILE(){
    
#    DIRECTORY="dev proc run sys etc media boot home mnt opt bin root srv tmp usr lib lib32 lib64 libx32 sbin var"
    DIRECTORY="etc home media mnt root sbin tmp usr /usr/bin var"
    
    for dir in $DIRECTORY;do
        
    
        if [ -d "/$dir" ];then
            DIR_FILES=$(ls -lA "/$dir"| awk '{print $9}' | grep "^\.")
            
            if [ "$DIR_FILES" != "" ];then
                DEBUG "$INFOW" "FOUND SUSPICIUS HIDDEN FILE/S in $dir: " 
                
                for files in $DIR_FILES;do
                
                    DEBUG "\t$INFOW" "$files"
                       get_file_status "/$dir/$files"
                
                done
            fi
            
            
            # DEBUG "$INFO" "$(du -shb "/$dir1" 2>/dev/null |awk '{print $1}' | sha1sum | awk '{print $1}' )"
#         DEBUG "$INFO" "Symlink file"
#         ls -lA "/$dir"
#         
#     elif [ -f "/$dir" ];then
#         DEBUG "$INFO" "Regular file"
#         ls -lA "/$dir"

        fi
    done
}

HIDEN_FILE
FIND_SUID_GUID


    

