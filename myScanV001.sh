# /bin/bash

echo "[*]Host_name       :" $(hostname)
echo "[*]Os_version      :" $(uname -v)
echo "[*]Architecture    :" $(uname -m)
echo "[*]Kernel          :" $(uname -r) | sed 's/-.*//'
echo "[*]OS_FULLNAME	 :" $(grep "^VERSION_ID=" /etc/os-release | awk -F= '{print $2}' |tr -d '"')
echo "[*]OS    :" $(grep "^VERSION=" /etc/os-release | awk -F= '{print $2}' |tr -d '"')
echo "[*]Default Shell  :" $SHELL
echo "[*]Generate from NMAP: "
// write to /use/share/scan
nmap -n -sS $ip -oX /usr/share/scan/$(date +"%m-%d-%y")

