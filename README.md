# Zendesk Command Line Search Application

Include a README
Just because you know how to run your app doesn’t mean the person looking at your test does. They can spend 20 minutes of their precious time reading your source code and reverse engineering it to work out where your main class is and the command to run it. Or you can just tell them. By not spelling it out you are moving your application closer to the reject pile. If you’re doing the test in a language they’re not currently working in then be more explicit with your instructions. If they’re not Rubyists then tell them which version of Ruby to install along with some instructions on how to install it. Likewise C compilers, Java package managers, .NET versioning and so on can all turn into a big time-sink of Googling, reading man pages and frustration. So be considerate, explicit and accurate in your README.


### Instructions

Using the provided data (tickets.json and users.json and organization.json ) write a simple command line application to search the data and return the results in a human readable format. Feel free to use libraries or roll your own code as you see fit. Where the data exists, values from any related entities should be included in the results. The user should be able to search on any field, full value matching is fine (e.g. “mar” won’t return “mary”). The user should also be able to search for empty values, e.g. where description is empty.
Search can get pretty complicated pretty easily, we just want to see that you can code a basic search application.

### Importing Data:

1. Install MongoDb  
   Instructions for Mac: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/
  

2. Import organizations.json into MongoDB   
   ```mongoimport --jsonArray --db test --collection organizations --file organizations.json```
  
   
3. Import tickets.json into MongoDB   
   ```mongoimport --jsonArray --db test --collection tickets --file tickets.json```
  
   
4. Import users.json into MongoDB   
   ```mongoimport --jsonArray --db test --collection users --file users.json ```
  
   
5. Install python mongo driver  
``` python -m pip install pymongo ```

### Installng Dependancies:

pip install -r requirements.txt

### Running the Application:


### Packaging the Application:
```
   pyinstaller main.py
   pyinstaller main.spec
```

### TODO

Comprehensive testing
Handle cases where the search value is not a string (eg an int or a bool)
Error Handling
Allow user to quit at any time




