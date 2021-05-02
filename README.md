# Command Line Search Application

__Author__: Anthony Nicholas  
__Date__: 25 February 2021  
__Version__: 1.0  

### Description

This Application provides command line search of the contents of three json files: tickets.json and users.json and organization.json.  The user is able to search each of these entities using any of the fields contained in thes json files.  Where the data exists, values from any related entities are included in the results. 

The Application has been built with Python using the following components:
* The __click__ python package: A library for building command line interactions https://click.palletsprojects.com/en/7.x/
* __TinyDB__: A python library providing for storage of documents as python dicts: https://tinydb.readthedocs.io/en/latest/.  This should provide good performance for the anticipated user load (10000+ users).  If the number of users was to go into the 100,000 or higher, consideration should be given to using a more advanced NoSql database such as MongoDb.

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

### Notes

When returning assocated data, I have assumed the relationship between users and tickets is via the submitter_id field on the ticket only.  I assume that the assignee_id field is related to staff, not users.




