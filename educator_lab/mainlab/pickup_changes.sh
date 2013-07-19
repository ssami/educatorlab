#!/bin/bash

PARAMS=$1
if [ -z "$PARAMS" ]
then 
	python2.7 manage.py schemamigration mainlab --auto
	echo ">>> If everything went well with that south migration, hit enter to continue. If not, hit Ctrl+C"
	read BLAH
	python2.7 manage.py migrate mainlab
	/home/sumitasami/webapps/educator_lab/apache2/bin/restart
else
	echo "Script that restarts apache in the webapps/apache dir, then migrates DB with South"
fi
