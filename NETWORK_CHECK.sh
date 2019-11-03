#!/bin/bash

CHECKDIR="[\033[32mCHECK\e[0m]"
INFO="[\033[34mINFO\e[0m]"
INFO_ACTIVE="[\033[32mDETECTED\e[0m]"
ACTIVE_HOST="[\033[32mHOST UP\e[0m]"
INFOW="[\033[31mINFO\e[0m]"
LOCALIP="[\033[34mLOCAL IP\e[0m]"
OK="[\033[32mOK\e[0m]"
WAIT="[\033[32m*\e[0m]"
WAR="[\033[31m!\e[0m]"

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

LOCAL_MACHINE_IP=""
LOOP_BACK="127.0.0.1"
LOCAL_LAN="192.168.1.0"
I_ETH="eth0"
I_WLAN="wlan0"
I_WLAN_mon="wlan0man"


# PORTS

P_FTP="21"
P_SSH="22"
P_SMTP="25"
P_HTTP="80"
P_POP="110"
P_SQL="3306"

HEADER $INFO "NETWORK DETAILS"

get_local_ip(){

    local ip=$(python3 script/ip.py)
    LOCAL_MACHINE_IP=$ip
    
    if [ "$ip" != "" ];then
        DEBUG "$LOCALIP $ip"
    else
        DEBUG  "$INFOW NO CONNECTED"
    fi
}

get_interface(){
    
    INTERFACE=($(netstat -i | awk '{print $1}'))
    # $INTERFACE | awk '{print $3}
    
    element_count=${#INTERFACE[@]}
    
    for i in $(seq 2 $(expr $element_count - 1));do
    
        echo -e "$INFO_ACTIVE ${INTERFACE[$i]}"
    done
}


find_host(){
    
    if [ "$LOCAL_MACHINE_IP" != "" ];then
        
        DEBUG "$INFOW" "CHECK LOCAL NETWORK: $LOCAL_LAN"
        
        nmap -n -sn "$LOCAL_LAN/24" -oX report/xml_raport.xml 1>/dev/null
        ACTIVE_HOSTS=($(python3 script/xml_parser.py))
        element_count=${#ACTIVE_HOSTS[@]}
    
        for i in $(seq 0 $(expr $element_count - 1));do
            DEBUG "$ACTIVE_HOST ${ACTIVE_HOSTS[$i]}"
        done
        
    else
            DEBUG "$INFOW" "No ip detected. Can't start scanning"
    fi
}


get_interface
get_local_ip
find_host
