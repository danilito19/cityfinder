cityfinder
========================

### What is this?
-------------

CS 122 project:
An application to recommend US cities to move to based on user preferences.

Requirements
-----------

* You are running OSX or unix machine.
* You are using Python 2.7.
* You are using a VirtualMachine where you will download requirements OR you have [virtualenv](https://pypi.python.org/pypi/virtualenv) and, if you'd like, [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper) installed and working.


Set Up
---------------

Either from your VM or within your virtualenv, to get all required packages, run
```
pip install -r requirements.txt
```

Using cityfinder
---------------

```cd ``` to the /cityfinder dir (where the file manage.py is) and run

```
python manage.py runserver
```
You can now open up localhost/8000/cityfinderapp in your browser and see the front-end

Code description
---------------
All relevant project code is within cityfinder directory.
/scripts contains code we used to clean or transform the data to put it into django's database. db_transform.py is legacy code, while import_data.py was the latest we used to update the database.

/cityfinderapp contains most of our work, including the Django application. algorithms.py and City.py are files with code we created to run a weighted-scores algorithm to rank cities according to user preference.

** INCLUDE DB IF NOT LARGE*
