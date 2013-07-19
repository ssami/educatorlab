#!/bin/bash


python2.7 manage.py schemamigration mainlab --auto
echo ">>> If everything went well with that south migration, hit enter to continue. If not, hit Ctrl+C"
read BLAH
python2.7 manage.py migrate mainlab
../apache2/bin/restart
