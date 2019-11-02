#!/bin/bash

OK="[\033[32mOK\e[0m]"
WAIT="[\033[32m*\e[0m]"
CHECKDIR="[\033[32mCHECK\e[0m]"
WAR="[\033[31m!\e[0m]"
INFO="[\033[34mINFO\e[0m]"
INFOW="[\033[31mINFO\e[0m]"
LOCALIP="[\033[34mLOCAL IP\e[0m]"

HEADER() {
echo ""
echo -e "----------- $1 $2  ------------" 
echo ""
}


LOCAL_IP="127.0.0.1"
I_ETH="eth0"
I_WLAN="wlan0"
I_WLAN_mon="wlan0man"


# PORTS

P_FTP="21"
P_HTTP="80"
P_POP="110"
P_SQL="3306"
P_SSH="22"
P_SMTP="25"

# ip netconf
# ip route

HEADER $INFO "NETWORK DETAILS"

get_local_ip(){
    ip=$(python ip.py)
    echo -e "$LOCALIP $ip"    
}

get_interface(){
    
    netstat -i | awk '{print $1}'

}





get_interface()

get_local_ip
