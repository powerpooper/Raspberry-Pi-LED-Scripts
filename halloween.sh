#!/bin/bash

hlwnon=$(echo "/usr/lib/cgi-bin/halloween.py")
varfile=$(echo "/usr/lib/cgi-bin/varfile.py")
hlwnpid=$(cat $varfile | grep -i halloween | awk -F=\  '{print$2}')


if [ "$1" == "on" ]
then
	sudo python $hlwnon > /dev/null 2>&1 &
fi

if [ "$1" == "off" ]
then
	sudo kill -SIGINT $hlwnpid
	sed -i "s/$hlwnpid/False/g" $varfile
#	sudo rm /usr/lib/cgi-bin/*.pyc
fi
exit 0
