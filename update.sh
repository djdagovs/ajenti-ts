#!/bin/bash
sudo cp -R  {*.py,layout/} /var/lib/ajenti/plugins/ajenti-ts/
sudo service ajenti restart
sleep 10
cat /var/log/ajenti/ajenti.log

