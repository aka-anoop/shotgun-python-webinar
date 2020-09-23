# Shotgun Python Webinar
Example code used for demonstrating various API features during Autodesk Shotgun Python Webinar

# Dependencies
- Virtualenv 
- Shotgun Python API
- Click
- Dotenv

# Project structure
Examples are organised under src directory in to separate chapter files.

# Usage
###  Setup local dev environment
- Setup Virtualenv `virtualenv venv`
- Activate Virtualenv `source venv/bin/activate`
- Install dependencies `pip install -r requirements.txt`

### Create new API Key
![Shotgun Script Dialog](/images/shotgun-script.png?raw=true "Shotgun Script Dialog")

###  Update API Key in the environment
Make a copy of `example.env` file included in the repository and name it `.env`
Update the file to include your Shotgun Script credentials. 
```
SERVER=<YOUR SERVER URL>
SCRIPT_NAME=`<YOUR SCRIPT NAME>
API_KEY=<YOUR API KEY>
```

Individual chapter code examples can be run from the repository top level directory by just executing `python src/demo{x}.py`

eg: `python src/demo1.py`
