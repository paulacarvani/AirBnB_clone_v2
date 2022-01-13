#!/usr/bin/env bash
# Script that prepares my web servers for deployment of the static site

# Install nginx if not installed already
sudo apt update && sudo apt install nginx -y

# Create all directories 
sudo mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML for testing nginx configuration
printf "\
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" | sudo tee /data/web_static/releases/test/index.html 

# Create a symlink linked to the /data/web_static/releases/test/ folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update the nginx config to serve the content of /data/web_static/current/
#   to hbnb_static.
sudo sed -i "/listen 80 default_server;/a \\\n\\tlocation /hbnb_static {\\n\\t\\talias /data/web_static/current/;\\n\\t}"\
       	/etc/nginx/sites-available/default

# Restart nginx
sudo service nginx restart
