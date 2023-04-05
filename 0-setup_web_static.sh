#!/usr/bin/env bash
# This script sets up my web servers for web_static deployment


# This command updates the packages with yes to every prompt
sudo apt-get -y update
sudo apt-get -y install nginx

# Configuring the firewall
sudo ufw allow 'Nginx HTTP'

# This command creates the directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Adding a fake html page
echo "<h1>This is allawake.tech</h1>" > /data/web_static/releases/test/index.html

# This command is to prevent overwrite
if [ -d "/data/web_static/current" ];
then
    echo "path /data/web_static/current exists"
    sudo rm -rf /data/web_static/current;
fi;

# This command creates the symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data

sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'

# This command restarts the nginx
sudo service nginx restart
