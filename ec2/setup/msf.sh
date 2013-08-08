#!/bin/sh
# Install metasploit framework
cd /opt
sudo git clone https://github.com/rapid7/metasploit-framework.git

cd metasploit-framework
sudo bash -c 'for MSF in $(ls msf*); do ln -s /opt/metasploit-framework/$MSF /usr/local/bin/$MSF;done'

curl -# -o /tmp/armitage.tgz http://www.fastandeasyhacking.com/download/armitage-latest.tgz
sudo tar -xvzf /tmp/armitage.tgz -C /opt
sudo ln -s /opt/armitage/armitage /usr/local/bin/armitage
sudo ln -s /opt/armitage/teamserver /usr/local/bin/teamserver

bundle install

#Probably doesn't even work
echo 'production:
   adapter: postgresql
   database: msf
   username: msf
   password: 
   host: 127.0.0.1
   port: 5432
   pool: 75
   timeout: 5' > database.yml

sudo sh -c "echo export MSF_DATABASE_CONFIG=/opt/metasploit-framework/database.yml >> /etc/profile"
source /etc/profile

echo It seems like msf is ready to go


