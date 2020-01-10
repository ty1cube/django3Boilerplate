# django Boilerplate

## Guide

#### Clone the repository

`git clone https://github.com/ty1cube/django3Boilerplate.git`

#### Create and activate virtual environment

    $ virtualenv env

##### On window

    $ cd venv/Scripts/activate 


##### On Linux or Mac

    $ cd venv/bin/activate 

### rename folder

Rename `django3Boilerplate`  to `src`

#### Change directory
    $ cd src

#### Install the requirement

    $ pip install -r requirements.txt

#### Rename the project folder

    $ python manage.py rename myproject

#### Migrate

    $ python manage.py migrate
#### create a static folder

Create `static_env` folder in `src `  directory

#### Collect static files

    $ python manage.py collectstatic

#### Runserver

    $ python manage.py runserver
