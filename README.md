# Simple flask app
This is a simple flask app fitted with 

This repository includes:
- Simple flask Application code
- Web frontend config code in `web-config` folder
- Pipeline code - includes `buildspec.yml` and `appspec.yml` files, and `scripts` folder

It uses nginx with gunicorn to serve flask application

The url_path
- /version - shows the version of the app in a json response
- /now - shows the current time in UTC