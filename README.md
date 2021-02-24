# Zendesk Command Line Search Application

Include a README
Just because you know how to run your app doesn’t mean the person looking at your test does. They can spend 20 minutes of their precious time reading your source code and reverse engineering it to work out where your main class is and the command to run it. Or you can just tell them. By not spelling it out you are moving your application closer to the reject pile. If you’re doing the test in a language they’re not currently working in then be more explicit with your instructions. If they’re not Rubyists then tell them which version of Ruby to install along with some instructions on how to install it. Likewise C compilers, Java package managers, .NET versioning and so on can all turn into a big time-sink of Googling, reading man pages and frustration. So be considerate, explicit and accurate in your README.


### Instructions

Using the provided data (tickets.json and users.json and organization.json ) write a simple command line application to search the data and return the results in a human readable format. Feel free to use libraries or roll your own code as you see fit. Where the data exists, values from any related entities should be included in the results. The user should be able to search on any field, full value matching is fine (e.g. “mar” won’t return “mary”). The user should also be able to search for empty values, e.g. where description is empty.
Search can get pretty complicated pretty easily, we just want to see that you can code a basic search application.


### Requirements

* Python version `>=3.5` is required.

### Create environment

Clone the repository & then navigate into the searchCLI directory.  Create a virtual environment in the repository with:

```sh
python3 -m venv .searchCLIenv
```

Activate the virtual environment & install the dependencies in the virtual environment:

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
pytest
```

### TODO

Comprehensive testing
Error Handling




