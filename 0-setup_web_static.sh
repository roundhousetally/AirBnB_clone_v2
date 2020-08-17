#!/usr/bin/env bash
# Task 0
sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir /data
sudo mkdir /data/web_static
sudo mkdir /data/web_static/releases
sudo mkdir /data/web_static/shared
sudo mkdir /data/web_static/releases/test

indx="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

sudo touch /data/web_static/releases/test/index.html
sudo echo "$indx" | sudo tee /data/web_static/releases/test/index.html

if [ ! -L /data/web_static/current ]; then
        sudo rm /data/web_static/current
        echo "in if"
fi
sudo ln -s /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data

srvr="^server {$"
repl="server {\
\n\tlocation /hbnv_static {\
\n\t\talias /data/web_static/current/;\
\n\t\tinternal;\
\n\t}\n"
file="/etc/nginx/sites-available/default"

sudo sed -i 's,'"$srvr"','"$repl"',' "$file"

sudo service nginx restart
