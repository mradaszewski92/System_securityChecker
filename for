#!/bin/bash

DATA="/bin /usr /tmp /home ."
for i in $DATA;do
	echo "------------ CHECK  $i ------------------"
	echo $(ls -la $i | awk '{print $9}')
	echo "------------------------------------"
done
