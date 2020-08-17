#!/usr/bin/env bash
# sets up web servers to deploy airbnb clone
apt-get update
apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared    
ufw allow 'Nginx HTTP'
sudo touch /data/web_static/releases/test/index.html 
echo "<h1>Fake Content as a test</h1>" | sudo tee /data/web_static/releases/test/index.html 
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i "45a \\\tlocation /hbnb_static {\n" /etc/nginx/sites-available/default
sed -i "46a \\\t\talias /data/web_static/current/;\n" /etc/nginx/sites-available/default
sed -i "47a \\\t}\n" /etc/nginx/sites-available/default 
sudo service nginx restart
