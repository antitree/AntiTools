#!/bin/sh
# Install and compile nmap
mkdir ~/Development
cd ~/Development
svn co https://svn.nmap.org/nmap
cd nmap
./configure
make
sudo make install
make clean
