## Photosplash Gallery 
This is an Independent project for Moringa Core Django module, may 29th 2022.

 ## Description
Photosplash is a photo gallery web application to showcase beautiful pictures. Users get can view photos uploaded by admin. Users can see photos based on the location, by clicking on the listed locations in the menu. They can also copy the link to a photo to paste for use. They can also search for photos based on the categories.

 ## Features
- The home page allows users to see various images:
- User can see all images per location they were taken
- Users can also search for images based categories
- Admin can upload images from a django dashboard
- View Live Site 
- View the complete site 

## Technologies Used
- Python 3.9
- Django MVC framework
- HTML, CSS and Bootstrap
- JavaScript
- Postgressql
- Heroku
 ## Specifications
To view the user directories or BDD check the specs file.

## Prerequisite
The Photosplash project requires a prerequisite understanding of the following:

- Django Framework
- Python3.9
- Postgres
- Python virtualenv
- Setup and installation
- Clone the Repo
- Activate virtual environment
- Activate virtual environment using python3.9 as default handler virtualenv -p /usr/bin/python3.9 venv && -  source venv/bin/activate

## Install dependancies
Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

Create the Database
- psql
- CREATE DATABASE gallery;
.env file
* Create .env file and paste paste the following filling where appropriate:

- SECRET_KEY = '<Secret_key>'
- DBNAME = 'gallery'
- USER = '<Username>'
- PASSWORD = '<password>'
- DEBUG = True
- Run initial Migration
- python3.9 manage.py makemigrations gallery
- python3.9 manage.py migrate
     * Run the app
- python3.9 manage.py runserver
- Open terminal on localhost:8000
 ## Known bugs
No known bugs so far. If found drop me an email.

 ##  Contributors
- Christine Nkatha
## Contact Information
nkathachristine456@gmail.com | christine.nkatha@student.moringaschool.com