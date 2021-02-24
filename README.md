# Zendesk Command Line Search Application

Include a README
Just because you know how to run your app doesn’t mean the person looking at your test does. They can spend 20 minutes of their precious time reading your source code and reverse engineering it to work out where your main class is and the command to run it. Or you can just tell them. By not spelling it out you are moving your application closer to the reject pile. If you’re doing the test in a language they’re not currently working in then be more explicit with your instructions. If they’re not Rubyists then tell them which version of Ruby to install along with some instructions on how to install it. Likewise C compilers, Java package managers, .NET versioning and so on can all turn into a big time-sink of Googling, reading man pages and frustration. So be considerate, explicit and accurate in your README.


### Description

This Application provides command line search of the contents of three json files: tickets.json and users.json and organization.json.  The user is able to search each of these entities using any of the fields contained in thes json files.  Where the data exists, values from any related entities are included in the results. 

The Application has been built with Python using the floowing components:
* The click python package: https://click.palletsprojects.com/en/7.x/
* TinyDB: https://tinydb.readthedocs.io/en/latest/

### Requirements

Python version `3.8`

Packages listed in requirements.txt - which should be installed following the steps below:

1. Clone the repository & then navigate into the searchCLI directory.  Create a virtual environment in the repository with:

```sh
python3 -m venv .searchCLIenv
```

2. Activate the virtual environment & install the dependencies in the virtual environment:

```sh
source .searchCLIenv/bin/activate

pip3 install -r requirements.txt
````

### Running the Zendesk Search Code

Run the project by navigating to the searchCLI directory and running:

```sh
python3 main.py
````


### Running tests

To run the tests, navigate to the searchCLI directory and run:

```sh
pytest -v
```




