# podcastsAPI
This api get information from url 'https://rss.itunes.apple.com/api/v1/us/podcasts/top-podcasts/all/100/explicit.json'. Show this information and search podcasts by artist name. Also save information to local JSON File and remove information from this file. All code was written on app.py file.
## Installation

The solution was created in a virtual environment with 
the following libraries using python version 3.8.5
:

```
click==7.1.2
Flask==1.1.2
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
Werkzeug==1.0.1

```

To enable virtual environment is necessary use next command on command prompt in project folder: 
```
venv\Scripts\activate.bat
```
We need configure flask application to execute and environment with next commands n command prompt:
```
set FLASK_APP=app.py
set FLASK_ENV=development
```

To run API on command prompt we need execute next command:
```
flask run
```

The api could be accessible on localhost port 5000. Sample:  http://127.0.0.1:5000/

## Functions
### get_podcasts_info
This function get information from podcasts json file on url https://rss.itunes.apple.com/api/v1/us/podcasts/top-podcasts/all/100/explicit.json also this function clean json to get only information about podcasts.

## Endpoints
### show_podcasts
This endpoint shows the total of podcasts obtained from the json file through the get_podcasts_info function using get method.
Sample: http://127.0.0.1:5000/api/v1/show_podcasts/
### show_podcasts_by_artist_name
This endpoint show the information get from json file about podcasts records of a artist defined. Artist name is used as search parameter through get method. The information is getting through get_podcasts_info function and filter by lambda expression to simplified search.
Sample: http://127.0.0.1:5000/api/v1/show_podcasts_by_artist_name/iHeartRadio
### save_top20_podcasts
This endpoint is used to save top 20 podcasts getted through get_podcasts_info function from JSON file on local JSON file in json folder. This endpoint use open function to create the json file and add information with json.dump function. This endpoint use POST method and return information added to json file.
Sample: http://127.0.0.1:5000/api/v1/save_top20_podcasts/
### save_top20_from_bottom_podcasts
This endpoint is used to save top 20 from bottom podcasts if top_20_podcasts.json file exist. Information is getted through get_podcasts_info function from JSON file on local JSON file in json folder. This enpoint use open function to create the json file and add information with json.dump function. This endpoint use POST method and return information added to json file.
Sample: http://127.0.0.1:5000/api/v1/save_top20_from_bottom_podcasts/
### remove_podcast
This endpoint remove a podcast on determinate position from top_20_podcasts.json if top_20_podcasts.json file exist. It read  information from file and remove podcast information on determinate position by position parameter next write file with new information without record determinate and return information added to json file.
Sample: http://127.0.0.1:5000/api/v1/remove_podcast/1
## Database
This project doesn't use a database. If you want to use it, it can be done through the flask-SQL Alchemy library to integrate the SQL-Alchemy orm, for flask-migrate migrations and make the necessary configurations.
## Authentication 
For authentication it is possible to use the flask-login or JWT library through flask-jwt.