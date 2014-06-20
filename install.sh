#!/bin/bash

#Download and install python-ts3

wget https://github.com/nikdoof/python-ts3/archive/master.zip
unzip master.zip
rm master.zip
cd python-ts3-master
sudo python setup.py install
cd ..
sudo rm -rf python-ts3-master

#install the actual plugin

sudo mkdir /var/lib/ajenti/plugins/ajenti-ts/
sudo cp -R  {*.py,layout/} /var/lib/ajenti/plugins/ajenti-ts/

#restart ajenti service
sudo service ajenti restart