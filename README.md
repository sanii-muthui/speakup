# Project Name
Speakup

## Author
Daniel Muthui

## Description
THis is an application that gives you the privilegde to post a pitch on different categories.In order to view a certain post or be able to add a post you need to create an account where you will receive email to confirm that you are registered and then login to the website and can either upvote(like) or downvote(dislike) suggested posts.

## User Stories

As a user you should be able to:
* Create an account that logs you in the speakup website
* See the selected or posted posts by other people
* You can upvote or downvote for a certain post
* You shld be able to see and submit a post

## SetUp / Installation Requirements
### Cloning
* In your terminal:
        
        $ git clone https://github.com/sanii-muthui/speakup.git
        $ cd speakup

## Installing the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python 
        
* Installing Flask and other Modules

        $ python3.6 -m pip install Flask
        $ python3.6 -m pip install Flask-Bootstrap
        $ python3.6 -m pip install Flask-Font-Mail
        $ python3.6 -m pip install Flask-upload
        $ python3.6 -m pip install Flask-login
        $ python3.6 -m pip install Flask-Alchemy
        $ python3.6 -m pip install Flask-Simplemde

        
        
* To run the application, copy to your terminal:

        $ chmod +x start.sh
        $ ./start.sh
        
## Testing the Application
* Inorder to run the tests for the files:
        $ python3.6 manage.py tests
        
## Technologies Used
* Python3.6
* Flask
* python3.6
* pip
* virtualenv(Flask)
* Bootstrap
* Postgressql
* Heroku for deployment

# contact and support
contact me on [saniimuthui](muthuisanii@gmail.com)

## License
iHub sanii &copy;2019 (https://github.com/sanii-muthui/)