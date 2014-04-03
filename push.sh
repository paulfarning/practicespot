#!/bin/bash

if [ $# -lt 2 ] ; then
	echo Enter host name:
	read HOST
	HOSTNAME=$HOST
	echo Enter directory name:
	read DIR
	AUDIODIR=$DIR
else
	HOSTNAME=$1
	AUDIODIR=$2
fi

scp -r ./$AUDIODIR $HOSTNAME:audio/$AUDIODIR

ssh $HOSTNAME bash -c "'
rm audio/$AUDIODIR/.DS_Store
zip -r -u audio/$AUDIODIR.zip audio/$AUDIODIR
mv audio/$AUDIODIR.zip audio/$AUDIODIR
echo "Start build"
python lib/build.py
echo "Complete"
'"
