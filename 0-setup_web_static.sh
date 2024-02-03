#!/usr/bin/env bash
# Diploy static website

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
	apt-get update
	apt-get -y install nginx
fi

# Create necessary folders
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html
echo "Nyanchwa you did it for symmone!" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Set ownership to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
nginx_config="/etc/nginx/sites-available/default"
sudo sed -i '/^[[:space:]]*server {/a\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' $nginx_config

# Restart Nginx
sudo service nginx restart
