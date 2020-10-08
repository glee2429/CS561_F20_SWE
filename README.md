# CS561 Software Engineering - Fall 2020
#### Project: Stock Portfolio Management App 
Project Description: The US stock market reaches a record high valuation due to the exponential growth of tech stocks, which can help young people with limited capital create an additional income source while the interest rate is near zero, and the price level is continuously rising. However, there's a significant gap in exposure and practice for stock trading. To alleviate this problem and expand the access to stock trading, we have decided to create a stock trading simulation game that allows people to understand the supply and demand sides and practice holding/buying/selling stocks to build their portfolio.
#### Team: Rohan Borkar, Adam Sunderman, Saurabh Satish Desai, Ga Young Lee
Roles & Responsibilities: 
* Rohan Borkar: Product Owner / Developer
* Adam Sunderman: Scrum Master / Developer
* Saurabh Satish Desai: Developer
* Ga Young Lee: Developer

## How to Get Started
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
```terminal
(venv) $ flask run
```


