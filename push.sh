#!/bin/bash

if [ $# -lt 2 ] ; then
	echo Enter host name:
	read HOST
	HOSTNAME=$HOST
	echo Enter directory name:
	read DIR
  FULLDIR=$DIR
else
  HOSTNAME=$1
  FULLDIR=$2
fi

AUDIODIR=$(basename $FULLDIR)

scp -r ./$FULLDIR $HOSTNAME:audio/$AUDIODIR

ssh $HOSTNAME bash -c "'
rm audio/$AUDIODIR/.DS_Store
zip -r -u -j audio/$AUDIODIR.zip audio/$AUDIODIR
mv audio/$AUDIODIR.zip audio/$AUDIODIR
echo "Start build"
python lib/build.py
echo "Complete"
'"
