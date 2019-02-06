# Example Django app which uses Dropbox API V2 

This django app was built with the [django-rest-framework](https://www.django-rest-framework.org/) and uses an example "players" model. Following scripts were included to perform the respective tasks.

- Django based REST API with one model. [sctask/players](https://github.com/maneeshsistla8/django-dropbox/tree/master/sctask/players)

- Script to send POST request to django app. [sctask/postreq.py](https://github.com/maneeshsistla8/django-dropbox/blob/master/sctask/postreq.py)

- Script to export model database to CSV file. [sctask/export.py](https://github.com/maneeshsistla8/django-dropbox/blob/master/sctask/export.py)

- Script to upload CSV file to Dropbox. (Used Python SDK for the API v2) [sctask/upload.py](https://github.com/maneeshsistla8/django-dropbox/blob/master/sctask/upload.py)

- BASH Script to run server, send request, export to CSV and upload to Dropbox all at once. [sctask/run.sh](https://github.com/maneeshsistla8/django-dropbox/blob/master/sctask/run.sh)

## Setting up

Clone this repo to your machine, then install all of the application's dependencies (specified in requirements.txt)
`pip install -r requirements.txt`

Follow the instructions in [this](https://www.dropbox.com/developers/documentation/python#tutorial) official tutorial for registering the Dropbox API app and generate the access token. Copy and paste the token in upload.py.
`access_token = '#'`

Change into sctask
`cd sctask`

Create admin account
`python manage.py createsuperuser`

then
`python manage.py makemigrations players`

to make migrations for the app, then run
`python manage.py migrate`

## Running the application

You can now visit the URL http://localhost:8000 in your web browser to view the app and add/edit entries as you wish.

Bash script included [run.sh] performs the following tasks :
- Runs the server
- Runs test script to post request (Modify postreq.py to edit payload as you wish)
- Checks for success
- Then runs the script to export database to csv file and runs the final script to upload the csv file to dropbox.

Make the bash script executable
`chmod u+x run.sh`

Run the bash script and expect timely confirmations of the tasks in the terminal.
`./run.sh`

run.sh uses `nohup`, hence to stop the server you will have to kill the process
`kill <process_id>`





  
  
  
