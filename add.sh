#!/bin/bash

if [ $# -eq 0 ] ; then
	echo Enter directory name:
	read NAME
	AUDIODIR=$NAME
else
	AUDIODIR=$1
fi

rm audio/$AUDIODIR/.DS_Store
zip -r -u audio/$AUDIODIR.zip audio/$AUDIODIR
mv audio/$AUDIODIR.zip audio/$AUDIODIR
python lib/build.py
