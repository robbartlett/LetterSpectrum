LetterSpectrum
=========

A simple exercise of Python, Flask, SQLite, and React

This is a project for learning and experimentation.  When I started this, I had no exposure to React, and only brief exposure to Python and Flask.  This was a fun project to play with different technologies.

Original Concept:
Develop a web application which contains a page that allows the user to enter a string of characters.
When the user submits the input, take each character and display a color to represent the character.
So if the user submits &quot;Hello World&quot; they would see a series of 11 color shapes (1 for each character,
including the space).

Additionally, keep track of the characters entered so far and allow a user to see the number of times
each character was submitted to the system. This value is a cumulative total for all users, so it will add
up as more and more users access this system.

Assumptions
-----------

* Colors can be random
* Colors can repeat
* Colors are persisted, so they show up the same for each letter every time
* "Color Shape" refers just to some visual representation of the character
* "Users" are anonymous (no need to track user-specific entriesre)
* Scalability isn't a factor
* There is no need for near-real-time updates from one user to the next: positive action (click) is satisfactory

Installation
------------

Install Python.
Install Pip
Install virtualenv

$ virtualenv flask

Install the flask extensions (Win use backslash):

$ flask/bin/pip install flask
$ flask/bin/pip install flask-sqlalchemy
$ flask/bin/pip install sqlalchemy-migrate
$ flask/bin/pip install flask-whooshalchemy
$ flask/bin/pip install flask-babel
$ flask/bin/pip install coverage


Running
-------

To run the application in the development web server execute `run.py` with the Python interpreter from the flask virtual environment.

