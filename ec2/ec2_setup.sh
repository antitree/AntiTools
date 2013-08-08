#!/bin/sh
# NOT EVEN TESTED
# Derived from http://www.darkoperator.com/installing-metasploit-in-ubunt/

sudo apt-get update
sudo apt-get upgrade

## apt dependencies
sudo apt-get install build-essential libreadline-dev  libssl-dev libpq5 libpq-dev libreadline5 libsqlite3-dev libpcap-dev openjdk-7-jre subversion git-core autoconf postgresql pgadmin3 curl zlib1g-dev libxml2-dev libxslt1-dev vncviewer libyaml-dev ruby1.9.3

## Gem dependencies
sudo gem install wirble sqlite3 bundler 

## Install nmap

## install postgres

## install metasploit
