# Zendesk Command Line Search Application

### Instructions

Using the provided data (tickets.json ​and u​ sers.json ​and ​organization.json ​) write a simple command line application to search the data and return the results in a human readable format. Feel free to use libraries or roll your own code as you see fit. Where the data exists, values from any related entities should be included in the results. The user should be able to search on any field, full value matching is fine (e.g. “mar” won’t return “mary”). The user should also be able to search for empty values, e.g. where description is empty.
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

### Running the Application:

import click

