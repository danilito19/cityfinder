cityfinder
========================

### What is this?
-------------

CS 122 project:
An application to recommend US cities to move to based on user preferences.

Requirements
-----------

* You are using Python 2.7.
* You are using a VirtualMachine where you will download requirements OR you have [virtualenv](https://pypi.python.org/pypi/virtualenv)
* All Python packages required are within requirements.txt


Set Up
---------------

To get all required packages, run
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

**How the database was made**
The data came in multiple csvs, which we had to clean-up to be able to put in the database. We used short bash scripts as well as some manual work in Sublime text (regex find-replace) to delete columns, change cities and states which were clearly wrong (Chicago was listed in Indiana!). The more data cleaning we did, the more cities were able to match when we created the relationship to the City model. We wanted to get close to having as many cities as the walk score file has (108), although some files, such as crime data, did not provide information for many of our 108 cities.

TODO:
---------------
There are still many interesting things we'd like to do with this project that we were unable to finish by our deadline.
* use sessions to save user input in the html so user can see it if she goes back pages
* improvements to the algorithm
* additional city data
* more visualizations
* having 2 users input preferences (partners)
* cities near each other feature


**CONTRIBUTORS**
[Alden Gobal](https://github.com/aldengolab)
[Anna Hazard](https://github.com/annalizhaz)
[Dani Litovsky Alcala](https://github.com/danilito19)

