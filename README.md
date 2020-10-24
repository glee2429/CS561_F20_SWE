# CS561 Software Engineering - Fall 2020
#### Project: Stock Portfolio Management App 
#### Team: Rohan Borkar, Adam Sunderman, Saurabh Satish Desai, Ga Young Lee

## How to Restart & Debug (For returning developers)
Given that you already downloaded the file, go to the directory and activate the virtual environment designed for development. 
1. Activate the virtual development
```terminal
$ source venv/bin/activate
```
2. Install the Python packages specified in requirements.txt 
(Please make sure to double-check the version and dependencies)
```terminal
(venv)$ pip install -r requirements.txt
```

3. Designate the script to run and specifications to run the program
```terminal
(venv)$ export FLASK_APP=app.py
(venv)$ export FLASK_ENV=development
```
4. Create the tables (e.g., stocks, users) in the SQLite database in your virtual environment.
```terminal
(venv)$ flask shell
```
##### Start by importing the database object and then create the database table using create_all:
```terminal
>>> from project import database
>>> database.create_all()
>>> quit()
```
5. Once the above steps are done, run the flask app in the development server
```terminal
(venv)$ flask run
```

## How to Get Started (For new developers)
1. Download the file and unzip it.
2. Create a directory.

```terminal
$ mkdir stock-portfolio-management
$ cd stock-portfolio-management
```

3. Check out the Python version installed. Ideally, Python 3.8.x is recommended in this project.
```terminal
$ python3 --version
Python 3.8.5
```
## Virtual Environment for Development
4. Virtual environments create an isolated configured setting for each project. In Python 3, a built-in module <code> venv </code> can be used for creating a virtual environments by running the command below.
```terminal
$ python3 -m venv venv
```
This command creates a folder "venv" that includes a Python interpreter and scripts for activating/deactivating the virtual environment. 
###### (You can also learn more about the importance of virtual environments in Python here: https://realpython.com/python-virtual-environments-a-primer/)


5. Start your virtual environment by following the command. 
```terminal
$ source venv/bin/activate
(venv) $
```
Then, you can find (venv) to the left of the prompt which indicates your virtual environment is successfully activated.

## Package Installation Using pip
Now that your virtual environment is created and activated, let's install the necessary packages for the project using pip. 

6. First, let's start with Flask.
```terminal
(venv) $ pip install flask
```
This command installs the package and dependencies, such as other packages required for Flask.

7. Save the requirements for future use by using the commands below.
```terminal
(venv)$ pip freeze

click==7.1.2
Flask==1.1.2
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
Werkzeug==1.0.1
```
Once the requirements for the project are returned in terminal, you can save them in txt file.
```terminal
(venv)$ pip freeze > requirements.txt
```
## Development Server Setup Using Flask
Flask offers development servers that comes with the package. In order to use this mode, we need to specify that the target we're interested in is <code> app.py </code> and specify that the server is in development mode by using the commands below. 
```terminal
(venv) $ export FLASK_APP=app.py
(venv) $ export FLASK_ENV=development
```

## Finally, let's run your Flask app on your local server!
Use the command below and go to <code> http://127.0.0.1:5000/</code> to check out your Flask app on your local server. 

```terminal
(venv) $ flask run

 * Serving Flask app "app.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: ***-***-***
```


