#!/bin/sh
# Setup Postgresql
sudo -s
su postgres

createuser msf -P -S -R -D
createdb -O msf msf
exit
exit

sudo /etc/init.d/postgres start
