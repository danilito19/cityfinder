cityfinder
========================

### What is this?
-------------

CS 122 project:
An application to recommend US cities to move to based on user preferences.

Requirements
-----------

* You are running OSX.
* You are using Python 2.7. 
* You have [virtualenv](https://pypi.python.org/pypi/virtualenv) and, if you'd like, [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper) installed and working.


Set Up
---------------

Assuming you already have a fork of this project, just pull from upstream

```
git pull upstream master
```

Get pip and virtualenv
```
easy_install pip
```
or,  
```
sudo easy_install pip
```
then 
```
pip install virtualenv
```
go to cityfinder directory and create a virtualenvironment called cityfinderenv
```
virtualenv cityfinderenv
```
To activate the environment

```
source cityfinderenv/bin/activate
```

To get all packages, run
```
pip install -r requirements.txt
```
Run this command frequently when you pull the repo again to make sure you have all the requirements up to date.

IMPORTANT NOTE:
run ```cat .gitignore``` to see the gitignore file. This file tells git to not include certain files. We never want to include the virtualenv file because it contains an entire version of Python. We also never want to include database (db, sql) files or large csv because it will take forever to load them. Work with these files through our Drive.

Add this point, you may choose to download and use virtualenvwrapper - I have not yet.
But to activate your virtualenv, you always have to run
```
source cityfinderenv/bin/activate
```
You will know you are working inside the virtualenv when the name of the env is in parenthesis at the beginning of the terminal command.

Using Django app
---------------

```cd ``` to the /cityfinder dir (where the file manage.py is) and run

```
python manage.py runserver
```
You can now open up localhost/8000 in your browser and see the front-end
